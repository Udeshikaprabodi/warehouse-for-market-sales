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