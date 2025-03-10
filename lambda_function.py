import json
import boto3
import os
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    # Initialize AWS Clients
    secrets_client = boto3.client('secretsmanager')
    ssm_client = boto3.client('ssm')

    # Retrieve environment variables
    secret_id = os.getenv('SECRET_ID')  # ARN of the secret
    parameter_name = os.getenv('PARAMETER_NAME')  # Name of the SSM parameter
    enable_rotation = os.getenv('ENABLE_ROTATION', 'false').lower() == 'true'  # Boolean flag for rotation

    response_data = {}

    # Retrieve secret from Secrets Manager
    try:
        secret_response = secrets_client.get_secret_value(SecretId=secret_id)
        response_data['Secret'] = secret_response['SecretString']
    except ClientError as e:
        response_data['Secret_Error'] = str(e)

    # Retrieve parameter from Parameter Store
    try:
        param_response = ssm_client.get_parameter(Name=parameter_name, WithDecryption=True)
        response_data['Parameter'] = param_response['Parameter']['Value']
    except ClientError as e:
        response_data['Parameter_Error'] = str(e)

    # Optionally trigger secret rotation
    if enable_rotation:
        try:
            secrets_client.rotate_secret(SecretId=secret_id)
            response_data['Rotation_Status'] = "Rotation triggered successfully"
        except ClientError as e:
            response_data['Rotation_Error'] = str(e)

    return {
        'statusCode': 200,
        'body': json.dumps(response_data)
    }
