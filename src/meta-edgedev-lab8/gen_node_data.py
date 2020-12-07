#!/bin/env python3

from time import sleep
from datetime import datetime, timezone
import paho.mqtt.client as paho
import threading
import random
import struct
import base64

class node:
    def __init__(self, node_id):
       self.node_id = node_id
       self.client = paho.Client()
       self.client.connect('localhost', 1883)

       self.x_gforce = None
       self.y_gforce = None
       self.z_gforce = None
    
    def publish_node(self):
        
        self.x_gforce = 0 + random.randint(-1024, 1024)
        self.y_gforce = -256 + random.randint(0, 80)
        self.z_gforce = 0 + random.randint(-1024, 1024)
        
        timestamp = datetime.now(tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
        payload = bytes(timestamp, 'utf-8')

        message_byte_array = struct.pack('>ix23sxfff', self.node_id, payload, self.x_gforce, self.y_gforce, self.z_gforce)
        message_base64 = base64.b64encode(message_byte_array)
        self.client.publish('nodes/nodedata', payload=message_base64, qos=1)

        sleep(0.02)

if __name__ == '__main__':
    num_nodes = 10
    node_list = list()
    threads = list()
    
    for i in range(num_nodes):
        node_list.append(node(i + 1))
    
    for i in range(250):
        for node in node_list:
            x = threading.Thread(target=node.publish_node())
            threads.append(x)
            x.start()
        
        for thread in threads:
            thread.join()
        

