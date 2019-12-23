import json
import codebase as cb
# import requests


def lambda_handler(event, context):

    input_payload = json.loads(event['body'])


    return {
        "statusCode": 200,
        "body": json.dumps({            
        "message": cb.process(input_payload),
        # "location": ip.text.replace("\n", "")
        }),
    }
