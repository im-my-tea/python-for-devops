import boto3
from zipfile import ZipFile as Z

ROLE_ARN = "arn:aws:iam::209042752946:role/DevOps-Lambda-Role"
FUNC_NAME = "MyFirstDevOpsLambda"


print("Zipping code...")
with Z('function.zip', 'w') as f:
    f.write('lambda_function.py')


print("Reading zip...")
with open('function.zip', 'rb') as z:
    zipped_code = z.read()


print("Deploying to AWS...")
client = boto3.client('lambda', region_name='us-east-1')

try:
    response = client.create_function(
        FunctionName=FUNC_NAME,
        Runtime='python3.9',
        Role=ROLE_ARN,
        Handler='lambda_function.lambda_handler',
        Code={'ZipFile': zipped_code}
    )
    print(f"Success! Function ARN: {response['FunctionArn']}")

except client.exceptions.ResourceConflictException:
    print("Function already exists. Updating code...")
    client.update_function_code(
        FunctionName=FUNC_NAME,
        ZipFile=zipped_code
    )
    print("Update Complete.")