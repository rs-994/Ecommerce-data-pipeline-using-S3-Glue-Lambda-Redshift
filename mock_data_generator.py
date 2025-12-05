# mock_data_generator.py
import csv
import random
from datetime import datetime, timedelta
import boto3
from io import StringIO

class MockDataGenerator:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client('s3')
        
        # Sample data for generation
        self.customer_ids = ['C12345', 'C12346', 'C12347']
        self.product_ids = ['P12345', 'P12346', 'P12347']
        self.payment_types = ['Credit Card', 'Debit Card', 'PayPal', 'Cash']
        self.statuses = ['Completed', 'Pending', 'Cancelled']
    
    def generate_transaction_data(self, date, num_records=100):
        """Generate mock transaction data for a specific date"""
        transactions = []
        
        for i in range(num_records):
            transaction = {
                'transaction_id': f'TXN{random.randint(100000000, 999999999)}',
                'customer_id': random.choice(self.customer_ids),
                'product_id': random.choice(self.product_ids),
                'quantity': random.randint(1, 5),
                'price': round(random.uniform(10.0, 100.0), 2),
                'transaction_date': date.strftime('%Y-%m-%d'),
                'payment_type': random.choice(self.payment_types),
                'status': random.choice(self.statuses)
            }
            transactions.append(transaction)
        
        return transactions
    
    def upload_to_s3(self, transactions, date):
        """Upload transaction data to S3 with hive partitioning"""
        # Create CSV string
        output = StringIO()
        fieldnames = ['transaction_id', 'customer_id', 'product_id', 'quantity', 
                     'price', 'transaction_date', 'payment_type', 'status']
        
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)
        
        # Create S3 key with hive partitioning
        year = date.year
        month = f"{date.month:02d}"
        day = f"{date.day:02d}"
        
        key = f"transactions/year={year}/month={month}/day={day}/transactions_{date.strftime('%Y-%m-%d')}.csv"
        
        # Upload to S3
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=key,
            Body=output.getvalue()
        )
        
        print(f"Uploaded {len(transactions)} transactions to s3://{self.bucket_name}/{key}")

def main():
    # Configure your bucket name here
    BUCKET_NAME = "ecommerce-transactions"  
    
    generator = MockDataGenerator(BUCKET_NAME)
    
    # Generate data for last 7 days
    for i in range(7):
        date = datetime.now() - timedelta(days=i)
        transactions = generator.generate_transaction_data(date, num_records=50)
        generator.upload_to_s3(transactions, date)

if __name__ == "__main__":
    main()