import streamlit as st

# Generate a pre-signed URL for a file
def generate_presigned_url(s3_client, bucket_name, file_name, expiration=3600):
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': file_name},
            ExpiresIn=expiration
        )
        return url
    except Exception as e:
        st.error(f"Error generating pre-signed URL: {e}")
        return None