import json
import boto3
client = boto3.client('lex-runtime')
def lambda_handler(event, context):
    # TODO implement
    response = client.post_text(
        botName='ScheduleAppointment',
        botAlias='prod',
        userId='userId',
        inputText=event['queryStringParameters']['q']
    )
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
