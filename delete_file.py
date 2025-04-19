import streamlit as st

# Delete a file from a bucket
def delete_file(s3_client, bucket_name, file_name):
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=file_name)
        st.success(f"File '{file_name}' deleted successfully.")
    except Exception as e:
        st.error(f"Error deleting file: {e}")