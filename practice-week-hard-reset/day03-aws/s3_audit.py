import boto3
from botocore.exceptions import ClientError

s3 = boto3.client('s3')
buckets = s3.list_buckets()

print(f"--STARTING S3 AUDIT--")

for bucket in buckets['Buckets']:
    name = bucket['Name']
    print(f"Auditing: {name}")
    encryption = "OFF"
    try:
        enc_res = s3.get_bucket_encryption(Bucket=name)
        rules = enc_res['ServerSideEncryptionConfiguration']['Rules']
        encryption = rules[0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
    except ClientError:
        encryption = "OFF"

    total_size = 0
    object_count = 0

    paginator = s3.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=name)

    for page in page_iterator:
        if 'Contents' in page:
            for obj in page['Contents']:
                total_size += obj['Size']
                object_count += 1

    print(f"   --> Encryption {encryption} | Files: {object_count} | Size: {total_size} bytes\n")