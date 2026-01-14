import boto3

LAMBDA_ARN = "arn:aws:lambda:us-east-1:209042752946:function:MyFirstDevOpsLambda"
RULE_NAME = "DevOps-2-Minute-Trigger"

events = boto3.client('events', region_name='us-east-1')
lambda_client = boto3.client('lambda', region_name='us-east-1')

print(f"Creating Rule: {RULE_NAME}...")
    
rule_response = events.put_rule(
    Name=RULE_NAME,
    ScheduleExpression='rate(2 minutes)', # Runs every 2 mins
    State='ENABLED'
)
print(f"Rule ARN: {rule_response['RuleArn']}")

try:
    lambda_client.add_permission(
        FunctionName=LAMBDA_ARN.split(":")[-1], # Extracts name from ARN
        StatementId=f"{RULE_NAME}-permission",
        Action='lambda:InvokeFunction',
        Principal='events.amazonaws.com',
        SourceArn=rule_response['RuleArn']
    )
    print("Permissions added.")
except lambda_client.exceptions.ResourceConflictException:
    print("Permission already exists. Skipping.")

events.put_targets(
    Rule=RULE_NAME,
    Targets=[
        {
            'Id': '1',
            'Arn': LAMBDA_ARN
        }
    ]
)
print("Target linked. Automation Active.")

response = events.list_rules()
print("--- Current Rules ---")
for rule in response['Rules']:
    print(rule['Name'], "-", rule['ScheduleExpression'])
print("---------------------")