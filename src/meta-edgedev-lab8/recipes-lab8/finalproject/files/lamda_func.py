import json
import boto3

db = boto3.resource('dynamodb', region_name='us-east-1')
table = db.Table('fall_status')

# A lamda event handler that handles DynamoDB updates
def lambda_handler(event, context):
    print(event)
    
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                handle_insert(record)
            
            elif record['eventName'] == 'MODIFY':
                continue

            elif record['eventName'] == 'REMOVE':
                continue
        
    except Exception as e: 
        print(e)

def table_item(timestamp, node_id, y_gforce):
    if (int(y_gforce) >= -181):
        return {
            'timestamp': timestamp,
            'node_id': node_id,
            'fall_status': 'True'
        }
    
    else:
        return {
            'timestamp': timestamp,
            'node_id': node_id,
            'fall_status': 'False'
        }

# Handles an insert event to a DynamoDB
def handle_insert(record):
    
    new_image = record['dynamodb']['NewImage']
    
    timestamp = new_image['node_data']['S']
    node_id = new_image['node_id']['S']
    
    x_gforce = new_image['x_gforce']['N']
    y_gforce = new_image['y_gforce']['N']
    z_gforce = new_image['z_gforce']['N']
    
    result = table.put_item(Item=table_item(timestamp, node_id, y_gforce))