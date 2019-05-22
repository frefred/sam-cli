import json

# import requests


def lambda_handler(event, context):

    ProductID = event[ 'pathParameters' ][ 'product' ]
    return {
        "statusCode": 200,
        "body": json.dumps( ProductID ),
    }
