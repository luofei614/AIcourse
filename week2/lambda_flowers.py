import json
import boto3
import uuid
#替换成自己区域的 endpoint
dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://dynamodb.us-east-1.amazonaws.com")
def lambda_handler(event, context):
    table = dynamodb.Table('flowers')
    item={
        'id':str(uuid.uuid4()),
        'FlowerType':event['currentIntent']['slots']['FlowerType'],
        'PickupDate':event['currentIntent']['slots']['PickupDate'],
        'PickupTime':event['currentIntent']['slots']['PickupTime'],
    }
    resp= table.put_item(Item=item)
    msg = "Your reservation has been completed, the pickup flowtype is " + event['currentIntent']['slots']['FlowerType']
    return {
        "sessionAttributes": {},
        "dialogAction": {
            "type":
            "Close",
            "fulfillmentState": "Fulfilled",
            "message": {
            "contentType": "PlainText",
            "content": msg
        }
    }

    }
