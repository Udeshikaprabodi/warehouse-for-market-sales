CREATE TABLE dim_branch (
    branch_id INT PRIMARY KEY,
    branch_name VARCHAR(50),
    location VARCHAR(100)
);

CREATE TABLE dim_date (
    date_id INT PRIMARY KEY,
    date DATE,
    day_of_week VARCHAR(15),
    month INT,
    year INT
);

CREATE TABLE dim_product (
    product_id INT PRIMARY KEY,
    product_name VARCHAR(100),
    category VARCHAR(50)
);

CREATE TABLE fact_sales (
    sale_id INT PRIMARY KEY,
    branch_id INT REFERENCES dim_branch(branch_id),
    product_id INT REFERENCES dim_product(product_id),
    date_id INT REFERENCES dim_date(date_id),
    sales_amount DECIMAL,
    quantity INT
);
