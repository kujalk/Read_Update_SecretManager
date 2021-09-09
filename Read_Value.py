import boto3
import logging
from botocore.exceptions import ClientError
import os
import json

logging.basicConfig(format="%(asctime)s :: [%(module)s] :: [%(levelname)s] :: %(message)s",level="INFO")
logger = logging.getLogger('log')

def read_secret(session,namespace):
    try:

        logger.info(f"Going to read the secret value from namespace {namespace}")
        response = session.get_secret_value(SecretId=namespace)
        status_code = response.get('ResponseMetadata','').get('HTTPStatusCode','')

        if(status_code == 200):
            logger.info(f"Secret Value is {json.loads(response.get('SecretString',''))}")
        else:
            raise Exception(f"Status code is {status_code}")

    except Exception as e:
        logger.error(f"Error while reading the secret from namespace {namespace} - {e}")

#Main Program
aws_access_key_id = ""
aws_secret_access_key = ""
aws_region = "ap-southeast-1"
namespace = "prod/databases/dbserver1"

try:
    logger.info(f"Script Started")
    session= boto3.client('secretsmanager', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name=aws_region)

    read_secret(session,namespace)
    
except Exception as e:
    logger.error(f"Error in main program : {e}")