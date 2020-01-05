import json
import codebase as cb
# import requests


def lambda_handler(event, context):

    input_payload = json.loads(event['body'])
    
    out = cb.process(input_payload)
    out = str(out)

    return {
        "statusCode": 200,
        "body": json.dumps({            
        "message": ""+out
        }),
    }
