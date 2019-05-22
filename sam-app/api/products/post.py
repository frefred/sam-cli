import json
import os
import boto3

# import requests

# handle log via cloudwatch ?

def lambda_handler(event, context):

    try:
        dynamodb = boto3.resource('dynamodb')
        productTable = dynamodb.Table( 'product' )

        try:
            productName = event[ 'queryStringParameters' ][ 'name' ]

            productTable.put_item(
                Item={
                    'id': productName,
                    'name': productName
                }
            )

            return {
                "statusCode": 200,
                "body": json.dumps( 1 ),
            }
        except:
           return {
               "statusCode": 406,
               "body": json.dumps( 0 ),
           }
    except:
        return {
            "statusCode": 500,
            "body": json.dumps( 0 ),
        }
