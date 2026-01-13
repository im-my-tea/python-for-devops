import boto3

ec2 = boto3.client('ec2', region_name='us-east-1')

def stop_dev_instances():
    # 1. Find Running Dev Servers
    print("Scanning for running Dev servers...")

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'tag:Env', 'Values': ['Dev']}
        ]
    )

    # 2. Extract IDs
    instances_to_stop = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances_to_stop.append(instance['InstanceId'])

    # 3. Action
    if len(instances_to_stop) > 0:
        print(f"Stopping instances: {instances_to_stop}")
        ec2.stop_instances(InstanceIds=instances_to_stop)
        print("Success! Money saved.")
    else:
        print("No running Dev instances found.")

# Run it
stop_dev_instances()