#!/usr/bin/env python3
from flask import Flask, render_template, request, redirect, url_for
from pydub import AudioSegment
from note_recognition import predict_note_starts, predict_notes
import signal
import os
import json

# The IP address for the MQTT Broker
mqtt_broker = '192.168.1.100'

# Configures the Flask application
app = Flask(__name__)

# Restricts file uploads to .wav and sets directory
app.config['UPLOAD_EXTENSIONS'] = ['.wav']
app.config['UPLOAD_PATH'] = 'uploads'

# Capture SIGTERM signal to stop background process
def sigterm_handler(sig, frame):
    raise(SystemExit)
signal.signal(signal.SIGTERM, sigterm_handler)

# Serves index page
@app.route('/')
def index():
    return render_template('index.html')

# Intakes a .wav file and runs processing scripts
# Sends processed data to an MQTT broker
@app.route('/', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    filename = uploaded_file.filename

    if filename != '':
        file_ext = os.path.splitext(filename)[1]

        # Ensures the file type is .wav
        if file_ext not in app.config['UPLOAD_EXTENSIONS']:
            abort(400)

        # Saves the file to local memory
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))

        # Audio processing scripts to obtain notes and timestamps
        song = AudioSegment.from_file(os.path.join(app.config['UPLOAD_PATH'], filename))
        song = song.high_pass_filter(80, order=4)
        starts = predict_note_starts(song)
        predicted_notes = predict_notes(song, starts)

        # A dictionary with notes and their corresponding play time
        data_msg = {(starts[i] / 1000): predicted_notes[i] for i in range(len(starts))}
        payload = json.dumps(data_msg)

        # Publishes note data to the broker
        client.publish('audio', payload, qos=1)

    return redirect(url_for('index'))

# Starts the MQTT client
client = paho.Client()
client.connect(mqtt_broker, 1883)
client.loop_start()

# Starts the Flask app
app.run()
