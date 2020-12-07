#!/usr/bin/env python3
import boto3
from boto3.dynamodb.conditions import Attr
import os

# Setup AWS parameters
device_name = os.uname().nodename
TABLE_NAME = 'finalProject397'
os.environ['AWS_SHARED_CREDENTIALS_FILE'] = '~/.aws/credentials'

# Open AWS DynamoDB table
db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table(TABLE_NAME)

def get_table_data():
    response = table.scan()
    
    items = response['Items']
    for item in items:
        x_gforce = int(item['x_gforce'])
        y_gforce = int(item['y_gforce'])
        z_gforce = int(item['z_gforce'])

        item['x_gforce'] = x_gforce
        item['y_gforce'] = y_gforce
        item['z_gforce'] = z_gforce
    
    return items

print(get_table_data())




