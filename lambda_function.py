import json

def lambda_handler(event, context):
    SnsEvent = event['Records'][0]['Sns']
    s3ObjectRecord = json.loads(SnsEvent['Message'])['Records'][0]
    return s3ObjectRecord
