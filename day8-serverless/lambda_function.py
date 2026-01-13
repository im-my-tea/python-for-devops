def lambda_handler(event, context):
    print("Hello from Local Deployment!")
    return {
        'statusCode': 200, 'body': 'Success'
    }

# if __name__ == "__main__":
#     print(lambda_handler(None, None))