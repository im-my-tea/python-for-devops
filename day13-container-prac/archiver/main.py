import boto3
import time
import os

BUCKET_NAME = "devops-bootcamp-e79a67" 
FILE_PATH = "/shared_data/secret_logs.txt"
S3_KEY = "logs/secret_logs_backup.txt"

s3 = boto3.client('s3')

print("--- ARCHIVER STARTED ---")

last_upload_time = 0

while True:
    # 1. Check if file exists
    if os.path.exists(FILE_PATH):
        # 2. Get file modification time
        mod_time = os.path.getmtime(FILE_PATH)
        
        # 3. If file is newer than last upload, upload it
        if mod_time > last_upload_time:
            print(f"New data detected. Uploading to {BUCKET_NAME}...")
            try:
                s3.upload_file(FILE_PATH, BUCKET_NAME, S3_KEY)
                print("✅ Backup Successful")
                last_upload_time = time.time() # Update timestamp
            except Exception as e:
                print(f"❌ Upload Failed: {e}")
    else:
        print("Waiting for file to be created...")

    time.sleep(10)
