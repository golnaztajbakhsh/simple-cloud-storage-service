import boto3
from botocore.exceptions import ClientError
from config import BUCKET_NAME

s3_client = boto3.client('s3')

def upload_file(file_name, object_name):
    try:
        s3_client.upload_file(file_name, BUCKET_NAME, object_name)
        return True
    except ClientError as e:
        print(e)
        return False

def download_file(object_name, file_name):
    try:
        s3_client.download_file(Bucket=BUCKET_NAME, Key=object_name, Filename=file_name)
        return True
    except ClientError as e:
        print(e)
        return False

def list_files():
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except ClientError as e:
        print(e)
        return []

def delete_file(object_name):
    try:
        s3_client.delete_object(Bucket=BUCKET_NAME, Key=object_name)
        return True
    except ClientError as e:
        print(e)
        return False
