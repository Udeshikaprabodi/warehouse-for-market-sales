import os
import boto3
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REDSHIFT_ENDPOINT = os.getenv("REDSHIFT_ENDPOINT")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_DB = os.getenv("REDSHIFT_DB")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT")
S3_BUCKET = os.getenv("S3_BUCKET")

import os
import boto3
import psycopg2
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
REDSHIFT_ENDPOINT = os.getenv("REDSHIFT_ENDPOINT")
REDSHIFT_USER = os.getenv("REDSHIFT_USER")
REDSHIFT_PASSWORD = os.getenv("REDSHIFT_PASSWORD")
REDSHIFT_DB = os.getenv("REDSHIFT_DB")
REDSHIFT_PORT = os.getenv("REDSHIFT_PORT")
S3_BUCKET = os.getenv("S3_BUCKET")

# Upload CSV to S3
def upload_to_s3(file_name, bucket, object_name=None):
    s3_client = boto3.client(
        "s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY
    )
    object_name = object_name or file_name
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"Uploaded {file_name} to S3 bucket {bucket}")
    except Exception as e:
        print(f"Error uploading {file_name}: {e}")

