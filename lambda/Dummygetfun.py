import json
import boto3 
from botocore.exceptions import ClientError

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Dummytable')  # Replace with your table name

def lambda_handler(event, context):
    try:
        response = table.scan()
       

        return {
            'statusCode': 200,
            'body': json.dumps({
                'success': True,
                'messages': response['Items']
            })
        }
    except ClientError as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'success': False, 'error': str(e)})
        }