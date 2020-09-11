#!/usr/bin/env python3

from pyftdi.i2c import I2cController, I2cPort
from bme280 import BME280
from time import sleep
from luma.core.interface.serial import ftdi_i2c
from luma.core.render import canvas
from luma.oled.device import ssd1306
from time import sleep
from PIL import ImageFont
from datetime import datetime, timezone
import paho.mqtt.client as paho
import struct
import base64
import signal

# Wrapper to support BME280 library
class FTDI_WRAPPER_I2C(I2cPort):

    def read_i2c_block_data(self, i2c_addr, register, length):
        return self.read_from(register, length)
    
    def write_i2c_block_data(self, i2c_addr, register, data):
        self.write_to(register, data)

# FTDI board string
ft232h_device = 'ftdi://ftdi:232h/1'

# Luma Core I2C Bus Controller
# Luma OLED connection
oled_i2c = ftdi_i2c(ft232h_device, 0x3C)
oled_dev = ssd1306(oled_i2c)

# Font used for OLED disply
oled_font = ImageFont.truetype('FreePixel.ttf', 16)

# FTDI I2C Bus Controller for BME280
pyftdi_i2c = I2cController()
pyftdi_i2c.configure(ft232h_device)

# Configure BME280 I2C port and override with wrapper
bme280_i2c = pyftdi_i2c.get_port(0x76)
bme280_i2c.__class__ = FTDI_WRAPPER_I2C

# BME280 sensor
bme280 = BME280(i2c_dev=bme280_i2c)

# Prints the published message number upon send
def on_publish(client, userdata, mid):
    print(f'mid: {str(mid)}')

# Paho MQTT client setup to connect to localhost
client = paho.Client()
client.on_publish = on_publish
client.connect('localhost', 1883)
client.loop_start()

# A function that chops a string decimal number at the hundreds place
def str_chop(string):
    old_str = str(string)
    new_str = ''
    count = 0
    chop = False
    
    for char in old_str:
        if (count <= 2):
            new_str += char
        else:
            break

        if ((char == '.') | chop == True):
            chop = True
            count += 1
    
    return new_str

# Captures a SIGTERM signal to stop a background process
def sigterm_handler(sig, frame):
    raise(SystemExit)

# Initializes the SIGTERM signal
signal.signal(signal.SIGTERM, sigterm_handler)

# Super loop
try:
    while True:
        # Obtains BME280 data and the collection timestamp in utc
        timestamp = datetime.now(tz=timezone.utc).timestamp()
        temperature = bme280.get_temperature() * 9.0 / 5.0 + 32.0
        pressure = bme280.get_pressure()
        humidity = bme280.get_humidity()
        
        # Combines data and timestamp into a printable format
        climate_data = '{d}\n{t}°F\n{p}hPa\n{h}%'.format(d=timestamp, t=str_chop(temperature), p=str_chop(pressure), h=str_chop(humidity))
        
        # Prints the data and timestamp to the OLED screen
        with canvas(oled_dev) as draw:
            draw.multiline_text((0, 0), climate_data, fill='white', font=oled_font)
        
        # Converts the BME280 data and timestamp into a 32bit binary number
        # Encodes the number with a base64 algorithm
        message_byte_array = struct.pack('>dxfffxx', timestamp, temperature, pressure, humidity)
        message_base64 = base64.b64encode(message_byte_array)

        # Publishes the BME280 data to the MQTT broker
        client.publish('sensorboard/rawdata', payload=message_base64, qos=1)
        sleep(1)

except (KeyboardInterrupt, SystemExit):
    print('\nStopped')