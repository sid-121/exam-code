# S3 Bucket Explorer

# Overview
 This Flask application lists the contents of an Amazon S3 bucket. It provides a REST API endpoint to retrieve files and directories from a specified S3 bucket.

# Features
  Lists contents of a specific S3 bucket.
  Supports querying by directory (prefix) to filter results.


# Prerequisites
  - Python 3: Ensure Python 3 is installed on your system.
  - AWS Credentials: Ensure AWS credentials are configured Or can use IAM roles if running on an AWS EC2 instance.
  - Update the bucket_name variable in script with your S3 bucket name.

# Installation
 Clone the Repository:
  -     git clone https://github.com/sid-121/exam-code.git
        cd exam-code


# Install Dependencies:
    pip install flask boto3
    apt-get install -y python3-pip
    

# Running the Application
 -     python3 code.py
The application will be available at http://0.0.0.0:5000.

API Endpoints
 - List Bucket Content: GET /list-bucket-content/ or GET /list-bucket-content/<path:path>
 - Retrieves the contents of the specified S3 bucket. If <path> is provided, it filters the contents based on the prefix.

# Error Handling
  - Logs errors to the console if S3 access fails or if there is a problem with the request.
