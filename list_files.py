import streamlit as st
from download_file import download_file
from presigned_url import generate_presigned_url
from delete_file import delete_file
import os
# List files in a specific bucket
def list_files(s3_client, bucket_name):
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        return [obj['Key'] for obj in response.get('Contents', [])]
    except Exception as e:
        st.error(f"Error listing files: {e}")
        return []

# List files section
def list_files_section(s3_client, bucket_name):
    st.header("List Files in Bucket")
    bucket_name = st.text_input("Enter Bucket Name", value=bucket_name)

    # Use session state to persist the file list
    if "files" not in st.session_state:
        st.session_state.files = []

    if st.button("List Files"):
        st.session_state.files = list_files(s3_client, bucket_name)

    if st.session_state.files:
        st.write(f"Files in bucket '{bucket_name}':")
        for file in st.session_state.files:
            col1, col2, col3, col4, col5 = st.columns([3, 2, 2, 2, 2])  # Adjust column widths as needed
            with col1:
                st.write(file)  # Display the file name
            with col2:
                # Download Button
                download_key = f"download_{file}"
                if st.button("Download", key=download_key):
                    download_file(s3_client, bucket_name, file)
            with col3:
                # Pre-Signed URL Button
                presigned_key = f"presigned_{file}"
                if st.button("Pre-Signed URL", key=presigned_key):
                    url = generate_presigned_url(s3_client, bucket_name, file)
                    if url:
                        st.success(f"Pre-Signed URL for '{file}': {url}")
            with col4:
                # Delete Button
                delete_key = f"delete_{file}"
                if st.button("Delete", key=delete_key):
                    delete_file(s3_client, bucket_name, file)
                    st.session_state.files = list_files(s3_client, bucket_name)  # Refresh the file list
                    st.rerun()  # Rerun to reflect changes
            with col5:
                # Permanent URL (if applicable)
                permanent_url = f"{os.getenv('LIARA_ENDPOINT_URL')}/{bucket_name}/{file}"
                st.markdown(f"[Permanent URL]({permanent_url})", unsafe_allow_html=True)
    else:
        st.write(f"No files found in bucket '{bucket_name}'.")