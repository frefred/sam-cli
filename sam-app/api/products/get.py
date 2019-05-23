import json
import boto3

def lambda_handler(event, context):

    try:
        dynamodb = boto3.resource('dynamodb')
        productTable = dynamodb.Table( 'product' )

        productID = event[ 'pathParameters' ][ 'product' ]

        if not productID:
            raise Exception( 'productId is empty' )

        product = productTable.get_item( Key={'id': productID } );

        return {
            "statusCode": 200,
            "body": json.dumps( product[ 'Item'] ),
        }

    except:
        return {
            "statusCode": 406,
            "body": json.dumps( 0 ),
        }