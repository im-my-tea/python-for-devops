import boto3
import os


bucket_name = "devops-bootcamp-e79a67"
s3 = boto3.client('s3')


def upload_files(file_name):
    if os.path.exists(file_name):
        print(f"Uploading {file_name}...")
        s3.upload_file(file_name, bucket_name, file_name)
        print("File Uploaded!")
    else:
        print("File not found locally.")


def list_files():
    print("\n--- Files in Bucket ---")
    files = s3.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in files:
        for i in files['Contents']:
            print(i['Key'])
    else:
        print("Bucket is empty!")

upload_files("upload_me.txt")
list_files()