import os
import boto3
from botocore.exceptions import NoCredentialsError, ClientError

# # uncomment to use in development mode and .env file
# from dotenv import load_dotenv
# # Load environment variables from .env file
# load_dotenv()

# Retrieve object storage configuration from environment variables
LIARA_ENDPOINT = os.getenv("LIARA_ENDPOINT")
LIARA_BUCKET_NAME = os.getenv("LIARA_BUCKET_NAME")
LIARA_ACCESS_KEY = os.getenv("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY = os.getenv("LIARA_SECRET_KEY")

# Initialize S3 client
s3_client = boto3.client(
    "s3",
    endpoint_url=LIARA_ENDPOINT,
    aws_access_key_id=LIARA_ACCESS_KEY,
    aws_secret_access_key=LIARA_SECRET_KEY
)

def upload_file(file_path, object_name=None):
    """Uploads a file to the specified bucket on Liara object storage."""
    if object_name is None:
        object_name = os.path.basename(file_path)

    try:
        s3_client.upload_file(file_path, LIARA_BUCKET_NAME, object_name)
        print(f"File '{file_path}' uploaded successfully as '{object_name}'")
    except FileNotFoundError:
        print("The specified file was not found.")
    except NoCredentialsError:
        print("Credentials not available.")
    except ClientError as e:
        print("Failed to upload file:", e)

# Usage example
file_path = "file.txt"
upload_file(file_path)
