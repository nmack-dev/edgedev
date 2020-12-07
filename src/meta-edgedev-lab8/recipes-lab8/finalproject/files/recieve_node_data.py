from decimal import Decimal
import base64
import paho.mqtt.client as paho
import struct
import json
import boto3
import os

mqtt_broker = '192.168.1.100'

def on_subscribe(client, userdata, mid, granted_qos):
    print(f"Subscribed: {str(mid)}")

def on_message(client, userdata, msg):
    payload = msg.payload.decode('utf-8')
    message_byte_array = base64.b64decode(payload)
    (node_id, timestamp, x_gforce, y_gforce, z_gforce) = struct.unpack('>ix23sxfff', message_byte_array)

    global table
    result = table.put_item(Item=table_item(node_id, timestamp.decode('utf-8'), x_gforce, y_gforce, z_gforce))
    if (result['ResponseMetadata']['HTTPStatusCode'] != 200):
        print('Error')
        exit(1)

def table_item(node_id, timestamp, x_gforce, y_gforce, z_gforce):
    return {
        'node_data': timestamp,
        'node_id': str(node_id),
        'x_gforce': Decimal(x_gforce),
        'y_gforce': Decimal(y_gforce),
        'z_gforce': Decimal(z_gforce)
    }
    
client = paho.Client()
client.on_subscribe = on_subscribe
client.on_message = on_message
client.connect(mqtt_broker, 1883)
client.subscribe('nodes/nodedata', qos=1)

device_name = os.uname().nodename
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '~/.aws/credentials'
s3_client = boto3.client('s3')
db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('finalProject397')
#result = table.put_item(Item=table_item(1, '32', 25, 55, 67))

try:
    client.loop_forever()

except KeyboardInterrupt:
    print('\rDone')