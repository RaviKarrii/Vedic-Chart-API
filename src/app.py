import json
import codebase as cb
# import requests


def lambda_handler(event, context):
    """
    Body Will be 

    [
  {
  "Male":
  {
    Year: '1993',
    Month: '09',
    Day: '16',
    Hour: '17',
    Min: '55',
    Lat:'16.989',
    Lon: '82.247'
    
  }
}
]
    """

    # try:
    #     ip = requests.get("http://checkip.amazonaws.com/")
    # except requests.RequestException as e:
    #     # Send some context about this error to Lambda Logs
    #     print(e)

    #     raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": str(cb.convert_angle(190)),
            # "location": ip.text.replace("\n", "")
        }),
    }
