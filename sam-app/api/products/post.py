import json
import boto3

# handle log via cloudwatch ?

def lambda_handler(event, context):

    try:
        dynamodb = boto3.resource('dynamodb')
        productTable = dynamodb.Table( 'product' )

        try:
            productName = event[ 'queryStringParameters' ][ 'name' ]

            if not productName:
                raise Exception( 'productName is empty ' )

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
