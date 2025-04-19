import os
import streamlit as st
from utils import get_s3_client
from list_files import list_files_section
from upload_file import upload_file_section

# Load environment variables
LIARA_ENDPOINT_URL = os.getenv("LIARA_ENDPOINT_URL")
LIARA_ACCESS_KEY = os.getenv("LIARA_ACCESS_KEY")
LIARA_SECRET_KEY = os.getenv("LIARA_SECRET_KEY")
BUCKET_NAME = os.getenv("BUCKET_NAME")

# Initialize S3 client
s3_client = get_s3_client()

# Main Streamlit app
def main():
    st.set_page_config(page_title="Liara S3 File Manager", layout="wide")
    st.title("Liara S3 File Manager")

    # Sidebar navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "List Buckets", "List Files", "Upload File"])

    if page == "Home":
        st.write("Welcome to the Liara S3 File Manager!")
        st.write("Use the sidebar to navigate to different functionalities.")

    elif page == "List Buckets":
        from utils import list_buckets
        st.header("List Buckets")
        buckets = list_buckets(s3_client)
        if buckets:
            st.write("Available Buckets:")
            for bucket in buckets:
                st.write(bucket)
        else:
            st.write("No buckets found.")

    elif page == "List Files":
        list_files_section(s3_client, BUCKET_NAME)

    elif page == "Upload File":
        upload_file_section(s3_client, BUCKET_NAME)

if __name__ == "__main__":
    main()