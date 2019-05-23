import json
import boto3

# log error in CloudWatch

def lambda_handler(event, context):
    try:

        dynamodb = boto3.resource('dynamodb')
        productTable = dynamodb.Table( 'product' )

        productID = event[ 'pathParameters' ][ 'product' ]
        productName = event[ 'queryStringParameters' ][ 'name' ]

        if not productID:
            raise Exception( 'productId is empty' )
        if not productName:
            raise Exception( 'productName is empty' )

        productTable.update_item( Key={'id': productID}, AttributeUpdates={ 'name': { 'Value' : productName } } )

        return {
            "statusCode": 200,
            "body": json.dumps( "put" ),
        }
    except:
        return {
            "statusCode": 406,
            "body": json.dumps( 0 ),
        }