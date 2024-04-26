import os
import boto3
from dotenv import load_dotenv
from fastapi import UploadFile


def __get_s3_client(access_key_id, secret_key, endpoint_url):
    client = boto3.client("s3",
                          aws_access_key_id=access_key_id,
                          aws_secret_access_key=secret_key,
                          endpoint_url=endpoint_url,
                          )
    return client


def __get_s3_client_from_settings():
    load_dotenv(dotenv_path=".env")

    access_key_id = os.getenv("S3_CLIENT_ID")
    secret_key = os.getenv("S3_SECRET_KEY")
    endpoint_url = os.getenv("S3_ENDPOINT_URL")
    return __get_s3_client(access_key_id, secret_key, endpoint_url)


try:
    client = __get_s3_client_from_settings()
except Exception as e:
    print(f"Error getting s3 client: {e}")
    client = None


def upload_file(file: UploadFile):
    if client is None:
        raise Exception("S3 client not initialized")

    client.upload_fileobj(file.file, os.getenv("S3_BUCKET_NAME"), file.filename)
