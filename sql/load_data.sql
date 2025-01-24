

COPY dim_branch
FROM 's3://kegalle-sales-data/dim_branch.csv'
CREDENTIALS 'aws_access_key_id=<AWS_ACCESS_KEY>;aws_secret_access_key=<AWS_SECRET_KEY>'
CSV IGNOREHEADER 1;

COPY dim_product
FROM 's3://kegalle-sales-data/dim_product.csv'
CREDENTIALS 'aws_access_key_id=<AWS_ACCESS_KEY>;aws_secret_access_key=<AWS_SECRET_KEY>'
CSV IGNOREHEADER 1;

COPY dim_date
FROM 's3://kegalle-sales-data/dim_date.csv'
CREDENTIALS 'aws_access_key_id=<AWS_ACCESS_KEY>;aws_secret_access_key=<AWS_SECRET_KEY>'
CSV IGNOREHEADER 1;

COPY fact_sales
FROM 's3://kegalle-sales-data/fact_sales.csv'
CREDENTIALS 'aws_access_key_id=<AWS_ACCESS_KEY>;aws_secret_access_key=<AWS_SECRET_KEY>'
CSV IGNOREHEADER 1;
