COPY dim_branch FROM 's3://kegalle-sales-data/dim_branch.csv'
CREDENTIALS 'aws_access_key_id=AKIAXEFUNKMCLMCWFI44;aws_secret_access_key=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'
CSV IGNOREHEADER 1;

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
S3_BUCKET = "kegalle-sales-data"

