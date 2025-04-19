import streamlit as st

# Download a file from a bucket
def download_file(s3_client, bucket_name, file_name):
    try:
        file_path = f"./{file_name}"
        s3_client.download_file(bucket_name, file_name, file_path)
        st.success(f"File '{file_name}' downloaded successfully.")
        return file_path
    except Exception as e:
        st.error(f"Error downloading file: {e}")
        return None