import json
import logging
import boto3
from botocore.exceptions import ClientError

# Configure logging for AWS CloudWatch
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    Scans the AWS environment for EC2 instances missing a 'Project' tag.
    """
    logger.info("Cloud Janitor: Starting AWS Resource Audit...")
    
    # Initialize the EC2 client
    ec2_client = boto3.client('ec2', region_name='us-east-1')
    uncompliant_instances = []
    
    try:
        # Fetch all EC2 instances
        response = ec2_client.describe_instances()
        
        for reservation in response.get('Reservations', []):
            for instance in reservation.get('Instances', []):
                instance_id = instance.get('InstanceId')
                tags = instance.get('Tags', [])
                
                # Verify compliance
                has_project_tag = any(tag['Key'] == 'Project' for tag in tags)
                
                if not has_project_tag:
                    logger.warning(f"Compliance Alert: Instance {instance_id} is missing the 'Project' tag.")
                    uncompliant_instances.append(instance_id)
                    
        logger.info(f"Audit complete. {len(uncompliant_instances)} non-compliant instances flagged.")
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Audit completed successfully',
                'flagged_instances': uncompliant_instances
            })
        }
        
    except ClientError as e:
        logger.error(f"AWS Credential/Permission Error: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Execution failed due to AWS IAM permissions.'})
        }