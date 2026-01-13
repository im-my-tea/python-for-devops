import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

# resp = ec2.run_instances(
#     ImageId='ami-07ff62358b87c7116',  # Example: Ubuntu 24.04 in us-east-1
#     InstanceType='t2.micro',
#     MinCount=1,
#     MaxCount=1,
#     TagSpecifications=[
#         {
#             'ResourceType': 'instance',
#             'Tags': [{'Key': 'Env', 'Value': 'Dev'}, {'Key': 'Name', 'Value': 'Python-Server'}]
#         }
#     ]
# )

# instance_id = resp['Instances'][0]['InstanceId']
# print(f"Server Started! ID: {instance_id}")


target_id = "i-044eba30e3b36c4b5" 

print(f"Terminating {target_id}...")

ec2.terminate_instances(InstanceIds=[target_id])

print("Server Terminated. No money lost.")