# E-COMMERCE DATA PIPELINE USING S3,GLUE,LAMBDA,REDSHIFT
This project involves building a sophisticated event-driven data ingestion and
transformation pipeline focusing on e-commerce transactional data. I have designed a
system using AWS services such as S3, Lambda, Glue, Redshift, to ingest, transform,
validate, and upsert data into Amazon Redshift for analytical purposes.

<img width="1015" height="248" alt="image" src="https://github.com/user-attachments/assets/28f8eb82-407d-4b17-a200-cd8bcf9ff945" />



# ● Mock Data Generation- script attached
○ Transaction Data: Generate daily transaction files in CSV format, stored using
the following hive-style partitioning in S3:
 <img width="975" height="303" alt="image" src="https://github.com/user-attachments/assets/67f4d6ca-c8a7-4eac-a0ed-c1e6562aed10" />

● Dimension Tables and Sample Records- Pre-load dim_customers, dim_products dimension tables into Redshift as part of the setup process. Setup Redshift cluster first.

 <img width="975" height="440" alt="image" src="https://github.com/user-attachments/assets/41caf01f-704b-4f7a-a06c-e79dc28c6611" />

 <img width="975" height="564" alt="image" src="https://github.com/user-attachments/assets/46652f1e-2c57-483f-b0c2-f6d4055225d8" />

 <img width="975" height="446" alt="image" src="https://github.com/user-attachments/assets/f0857d08-250c-42c3-a1ad-398d627dad6c" />




 
 

# ● Data Ingestion and Transformation with AWS Glue
# ○ Event-Driven Ingestion: Configure an AWS Lambda function to trigger AWS Glue jobs upon detecting new files in the S3 transactions folder.

<img width="975" height="428" alt="image" src="https://github.com/user-attachments/assets/cc99b3d6-95ee-4b15-8de8-2a6aeb96cff7" />

 
# ● Data Transformation and Validation using Glue ETL

Establish Glue connection to Redshift by creating VPC endpoint
 
 <img width="975" height="159" alt="image" src="https://github.com/user-attachments/assets/399ce6b2-7991-44cf-a3cc-24dee982aa88" />
 <img width="975" height="354" alt="image" src="https://github.com/user-attachments/assets/2ebff701-ca5f-4ad9-965e-5c7ebcd3787f" />



# ○ Join Operations: Enrich transactional data by joining with dim_products and dim_customers based on product_id and customer_id.
# ○ Data Validation: Include validation logic in the Glue job to filter out transactions with invalid customer_id or product_id (e.g., missing in dimension tables).
# ○ Additional Transformations: Calculate the total transaction amount (quantity *price) and categorize transactions into different classes based on the amount (e.g., "Small", "Medium", "Large").
# ○ Upsert Operation in Amazon Redshift
 ○ Design the Glue job to perform an upsert operation into the fact_transactions
table in Redshift, using transaction_id as the key. Consider transaction date and
status when determining if an existing record should be updated.
 <img width="975" height="472" alt="image" src="https://github.com/user-attachments/assets/f3fe48ab-8038-4602-b6d2-7412057b3800" />

# Additional steps 
Add glue crawler info- add crawlers for both source and target to get their schema
Security group of in redshift has inbound rule open
S3 endpoint in VPC-In addition to s3 endpoint- u should also try setting up cloudwatch endpoint and glue endpoint in redshift vpc
Turn on aws eventbridge option in S3, TO SEND S3 NOTIFICATIONS TO EVENTBRIDGE
While creating crawler for redshift or target table, choose JDBC as data source and then give redshift glue connection name .

 









