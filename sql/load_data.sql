

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET = "kegalle-sales-data"

# SQL COPY commands with environment variables
COPY_DIM_BRANCH = f"""
COPY dim_branch FROM 's3://{S3_BUCKET}/dim_branch.csv'
CREDENTIALS 'aws_access_key_id={AWS_ACCESS_KEY};aws_secret_access_key={AWS_SECRET_KEY}'
CSV IGNOREHEADER 1;
"""

COPY_DIM_DATE = f"""
COPY dim_date FROM 's3://{S3_BUCKET}/dim_date.csv'
CREDENTIALS 'aws_access_key_id={AWS_ACCESS_KEY};aws_secret_access_key={AWS_SECRET_KEY}'
CSV IGNOREHEADER 1;
"""
