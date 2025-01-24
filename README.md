# supermarket-sales-warehouse

A project demonstrating the design and implementation of a data warehouse for consolidating historical sales data from three supermarket branches into a single repository using Amazon Redshift. Includes data schema design, ETL processes, and analytical queries to enable predictive insights and reporting.

## Objectives
- Understand and apply the principles of data warehousing.
- Design data schemas optimized for analytical processing (OLAP).
- Gain hands-on experience with Amazon Redshift and data warehouse technologies.
- Prepare the data for predictive analytics by structuring it in a consolidated format.

## Tools & Technologies
- **Amazon Redshift**: Cloud data warehousing.
- **Python**: For data preprocessing and loading.
- **SQL**: For querying and schema creation.
- **AWS S3**: For staging CSV data before loading into Redshift

## Dataset
The dataset represents historical sales data from three supermarket branches over three months. It includes fields like Invoice ID, Branch, City, Customer Type, Gender, Product Line, Unit Price, Quantity, Tax, Total, Date, Time, Payment, and Rating.

## Instructions
1. Prepare the data by cleaning and storing it in an AWS S3 bucket.
2. Set up an Amazon Redshift cluster and configure a database.
3. Design a star schema with fact and dimension tables.
4. Load the data using the COPY command in Redshift.
5. Run analytical queries to extract insights.

## Example Query
```sql
SELECT branch, SUM(total) AS total_sales
FROM sales_fact
JOIN branch_dim ON sales_fact.branch_id = branch_dim.branch_id
GROUP BY branch;
```

## Repository Structure
```
- README.md
- setup.md
- data/
  - sample_sales.csv
- sql/
  - create_schema.sql
  - load_data.sql
  - queries.sql
- notebooks/
  - data_preprocessing.ipynb
```

## License
This project is licensed under the MIT License.

## Acknowledgments
Dataset sourced from public domain data on supermarket sales in Kegalle.



