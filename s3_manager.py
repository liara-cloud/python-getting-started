import os
import boto3
from botocore.exceptions import ClientError
from typing import List, Dict

# use dotenv if needed
from dotenv import load_dotenv
load_dotenv()

class S3Manager:
    
    def __init__(self):
        self.endpoint_url = os.getenv('LIARA_ENDPOINT_URL')
        self.access_key = os.getenv('LIARA_ACCESS_KEY')
        self.secret_key = os.getenv('LIARA_SECRET_KEY')
        self.bucket_name = os.getenv('BUCKET_NAME')
        
        if not all([self.endpoint_url, self.access_key, self.secret_key, self.bucket_name]):
            raise ValueError("Missing required environment variables. Please check your .env file.")
        
        self.s3_client = boto3.client(
            's3',
            endpoint_url=self.endpoint_url,
            aws_access_key_id=self.access_key,
            aws_secret_access_key=self.secret_key
        )
    
    def list_files(self) -> List[Dict]:
        try:
            response = self.s3_client.list_objects_v2(Bucket=self.bucket_name)
            
            if 'Contents' not in response:
                return []
            
            files = []
            for obj in response['Contents']:
                files.append({
                    'key': obj['Key'],
                    'size': obj['Size'],
                    'last_modified': obj['LastModified'].isoformat(),
                    'etag': obj['ETag'].strip('"')
                })
            
            return files
        except ClientError as e:
            raise Exception(f"Error listing files: {str(e)}")
    
    def download_file(self, key: str, download_path: str) -> bool:
        try:
            self.s3_client.download_file(self.bucket_name, key, download_path)
            return True
        except ClientError as e:
            raise Exception(f"Error downloading file: {str(e)}")
    
    def delete_file(self, key: str) -> bool:
        try:
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=key)
            return True
        except ClientError as e:
            raise Exception(f"Error deleting file: {str(e)}")
    
    def generate_presigned_url(self, key: str, expiration: int = 3600) -> str:
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': key},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            raise Exception(f"Error generating presigned URL: {str(e)}")
    
    def get_permanent_url(self, key: str) -> str:
        endpoint = self.endpoint_url.replace('https://', '')
        return f"https://{self.bucket_name}.{endpoint}/{key}"
    
    def upload_file(self, file_path: str, key: str) -> bool:
        try:
            self.s3_client.upload_file(file_path, self.bucket_name, key)
            return True
        except ClientError as e:
            raise Exception(f"Error uploading file: {str(e)}")
    
    def upload_fileobj(self, file_obj, key: str) -> bool:
        try:
            self.s3_client.upload_fileobj(file_obj, self.bucket_name, key)
            return True
        except ClientError as e:
            raise Exception(f"Error uploading file: {str(e)}")