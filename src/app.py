import json
from .response import handler
# import requests


def lambda_handler(event, context):

    result = {
            "message": event['pathParameters']['Name'],
            # "location": ip.text.replace("\n", "")
        }
    
    handler(200,result)
