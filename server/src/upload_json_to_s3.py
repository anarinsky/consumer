import boto3
import json
import os


def load_aws_config(config_path):
    """
    Loads AWS configuration from a specified JSON file.

    Parameters:
    - config_path: Path to the config file.

    Returns:
    A dictionary with AWS configuration.
    """
    with open(config_path) as config_file:
        return json.load(config_file)

def upload_json_to_s3(bucket_name, s3_key, data, config_path='aws_config.json'):
    """
    Uploads a JSON string to an AWS S3 bucket, using credentials from a config file
    when not running on AWS Lambda.

    Parameters:
    - bucket_name: The name of the S3 bucket.
    - s3_key: The S3 key (path and file name) where the JSON should be stored.
    - data: The data to be converted into JSON and uploaded.
    - config_path: Path to the AWS configuration file. Default is 'aws_config.json'.
    """

    # Check if running on AWS Lambda by checking for the Lambda runtime API in environment variables
    if 'AWS_LAMBDA_RUNTIME_API' in os.environ:
        # Running on Lambda, use the execution role for credentials
        s3_client = boto3.client('s3')
    else:
        # Not running on Lambda, load credentials from a config file
        aws_config = load_aws_config(config_path)
        s3_client = boto3.client(
            's3',
            aws_access_key_id=aws_config['aws_access_key_id'],
            aws_secret_access_key=aws_config['aws_secret_access_key'],
            region_name=aws_config['region_name']
        )

    # Convert the data to a JSON string
    json_string = json.dumps(data)

    # Upload the JSON string to S3
    s3_client.put_object(Body=json_string, Bucket=bucket_name, Key=s3_key)

    print("Upload completed successfully")


# Example usage
bucket_name = 'your-bucket-name'
s3_key = 'your-file-name.json'
data = {"key": "value"}

# Call the function without specifying the config_path if running on Lambda
upload_json_to_s3(bucket_name, s3_key, data)
