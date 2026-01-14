import boto3
import botocore
import uuid


s3 = boto3.client('s3')
ec2 = boto3.client('ec2', region_name='us-east-1')


# --- PART 1: Safe Bucket Creator ---
def safe_create_bucket(name):
    print(f"\n--- Attempting to create: {name} ---")
    try:
        s3.create_bucket(Bucket=name)
        print(f"✅ Success: Created {name}")
    except s3.exceptions.BucketAlreadyExists:
        print(f"⚠️  Error: Bucket {name} globally exists (someone else owns it).")
    except s3.exceptions.BucketAlreadyOwnedByYou:
        print(f"ℹ️  Info: You already own {name}. Skipping...")
    except botocore.exceptions.ClientError as e:
        print(f"❌ Error: {e}")


# --- PART 2: EC2 Auditor ---
def audit_infrastructure():
    print("\n--- Auditing EC2 Infrastructure ---")
    response = ec2.describe_instances()
    
    count = 0
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            count += 1
            instance_id = instance['InstanceId']
            state = instance['State']['Name']
            inst_type = instance['InstanceType']
            
            # SAFE GET: Stopped instances don't have Public IPs. 
            # .get() prevents the crash.
            public_ip = instance.get('PublicIpAddress', 'N/A')
            
            print(f"ID: {instance_id} | Type: {inst_type} | State: {state} | IP: {public_ip}")
            
    if count == 0:
        print("No EC2 instances found.")


# --- PART 3: The Nuke Script (Cleanup) ---
def cleanup_lab():
    print("\n--- Starting Cleanup Protocol ---")
    response = s3.list_buckets()
    
    for bucket in response['Buckets']:
        name = bucket['Name']
        
        # SAFETY FILTER: Only touch buckets starting with our prefix
        if name.startswith("devops-bootcamp-"):
            print(f"Cleaning {name}...")
            
            # Step A: Empty the bucket (Required before deletion)
            objects = s3.list_objects_v2(Bucket=name)
            if 'Contents' in objects:
                files_to_delete = [{'Key': obj['Key']} for obj in objects['Contents']]
                s3.delete_objects(Bucket=name, Delete={'Objects': files_to_delete})
                print(f" - Deleted {len(files_to_delete)} files inside.")
            
            # Step B: Delete the bucket
            s3.delete_bucket(Bucket=name)
            print(f"🔥 Deleted Bucket: {name}")
        else:
            print(f"Skipping {name} (Safety Filter Active)")

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # 1. Test Creation
    unique_name = f"devops-bootcamp-{uuid.uuid4().hex[:6]}"
    safe_create_bucket(unique_name)
    
    # 2. Test Audit
    audit_infrastructure()
    
    # 3. Test Cleanup (Uncomment to run)
    cleanup_lab()