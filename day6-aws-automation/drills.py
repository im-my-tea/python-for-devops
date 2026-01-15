import boto3
import uuid


s3 = boto3.client('s3')

print("Connection Successful!")

bucket_name = f"devops-bootcamp-{uuid.uuid4().hex[:6]}"
# print(f"Creating bucket: {bucket_name}")
# s3.create_bucket(Bucket=bucket_name)

print(f"Bucket {bucket_name} Created.")

response = s3.list_buckets()
print(response['Buckets'])