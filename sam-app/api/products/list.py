import json
import boto3

# import requests

def lambda_handler(event, context):
    try:
        dynamodb = boto3.resource('dynamodb')
        productTable = dynamodb.Table( 'product' )

        try:
            products = []
            response = productTable.scan(AttributesToGet=[ 'name'])

            for i in response['Items']:
                products.append( i[ 'name' ] )

            return {
                "statusCode": 200,
                "body": json.dumps( products ),
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