# Liara S3 File Manager

This is a Streamlit-based application for managing files in an S3-compatible object storage service (e.g. Liara). The app allows you to list, upload, download, generate pre-signed URLs, and delete files directly from a web interface.

---

## Table of Contents

1. [Prerequisites](#prerequisites)
2. [Installation](#installation)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Set Up Environment Variables](#step-2-set-up-environment-variables)
   - [Step 3: Install Dependencies](#step-3-install-dependencies)
3. [Running the App](#running-the-app)
4. [Using the App](#using-the-app)
5. [Contributing](#contributing)


---

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.12 or higher
- Git (for cloning the repository)
- Streamlit: A Python library for building interactive web apps.
- Boto3: A Python library for interacting with AWS S3-compatible services.

Additionally, you need access to an S3-compatible storage service (e.g., Liara) with the following credentials:
- Endpoint URL
- Access Key
- Secret Key
- Bucket Name

---

## Installation

### Step 1: Clone the Repository

Clone the repository to your local machine using Git:

```
git clone https://github.com/liara-cloud/python-getting-started.git
```

Switch the branch to `objectStorage`:

```
git checkout objectStorage
```

---

### Step 2: Set Up Environment Variables

The app requires environment variables for authentication and configuration. rename `.env.example` to `.env` and set ENVs.

---

### Step 3: Install Dependencies

Install the required Python libraries.

```
pip install -r requirements.txt
```


---

## Run the App

Start the Streamlit app.

Once the app starts, it will provide a local URL (e.g. `http://localhost:8501`). Open this URL in your browser to interact with the app.

---

## Using the App

1. **Home Page**
- Displays a welcome message and navigation instructions.

2. **List Buckets**
- Lists all available buckets in your S3-compatible storage.

3. **List Files**
- Enter the bucket name and click "List Files" to see the files in the bucket.
- Perform actions like downloading, generating pre-signed URLs, or deleting files directly from the interface.

4. **Upload File**
- Select a file using the file uploader and click "Upload" to add it to the specified bucket.

---

## Contributing

Contributions are welcome! If you find a bug or want to add a feature:
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

