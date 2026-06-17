# ☁️ AWS Cloud Janitor: Resource Compliance Auditor

![AWS Lambda](https://img.shields.io/badge/AWS_Lambda-FF9900?style=for-the-badge&logo=aws-lambda&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3_SDK-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

An automated serverless compliance tool built with Python and the AWS Boto3 SDK. This project acts as a cloud governance script, scanning an AWS environment for EC2 instances that fail to comply with organizational tagging policies.

## 🎯 Project Overview
In enterprise AWS environments, untagged resources lead to billing confusion and management overhead. **Cloud Janitor** solves this by automatically querying the AWS API to identify active EC2 instances missing mandatory metadata (e.g., the `Project` tag) and logging them for review.

## 📂 Repository Structure
* `src/lambda_function.py`: The core automation logic designed for AWS Lambda execution.
* `requirements.txt`: Standard SDK dependencies for local testing.

## 🚀 How to Run Locally

To review or test this codebase on your own machine:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Gokuldas-dev/Python_AWS_Automation_Project_1_Cloud_Janitor.git](https://github.com/Gokuldas-dev/Python_AWS_Automation_Project_1_Cloud_Janitor.git)
