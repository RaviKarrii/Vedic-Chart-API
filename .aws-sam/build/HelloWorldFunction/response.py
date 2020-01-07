import json

# import requests


def handler(statusCode, message):
    return {
        "statusCode": statusCode,
        "body": json.dumps(message),
    }
