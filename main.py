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

# Execute SQL commands
def execute_redshift_query(query):
    try:
        conn = psycopg2.connect(
            host=REDSHIFT_ENDPOINT.split(":")[0],
            dbname=REDSHIFT_DB,
            user=REDSHIFT_USER,
            password=REDSHIFT_PASSWORD,
            port=REDSHIFT_PORT,
        )
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        print("Query executed successfully.")
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Error executing query: {e}")     

# Main Workflow
if __name__ == "__main__":
    # Step 1: Upload data to S3
    upload_to_s3("data/supermarket_sales.csv", S3_BUCKET, "supermarket_sales.csv")
    # Step 2: Run SQL scripts
    with open("sql/create_tables.sql", "r") as f:
        create_table_queries = f.read()
    execute_redshift_query(create_table_queries)
    
    with open("sql/load_data.sql", "r") as f:
        load_data_queries = f.read().replace(
            "<AWS_ACCESS_KEY>", AWS_ACCESS_KEY
        ).replace("<AWS_SECRET_ACCESS_KEY>", AWS_SECRET_KEY)
    execute_redshift_query(load_data_queries)