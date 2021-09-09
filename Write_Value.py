import boto3
import logging
from botocore.exceptions import ClientError
import os
import json

logging.basicConfig(format="%(asctime)s :: [%(module)s] :: [%(levelname)s] :: %(message)s",level="INFO")
logger = logging.getLogger('log')

def write_secret(session,namespace,secret):
    try:
        logger.info(f"Going to update the secret value for namespace {namespace}")
        
        response = session.get_secret_value(SecretId=namespace)
        status_code = response.get('ResponseMetadata','').get('HTTPStatusCode','')

        if(status_code == 200):

            old_secret = json.loads(response.get('SecretString',''))
            dict_secret= json.loads(secret)
            new_secret = json.dumps({**old_secret,**dict_secret})

            response = session.put_secret_value(SecretId=namespace,SecretString=str(new_secret))
            status_code = response.get('ResponseMetadata','').get('HTTPStatusCode','')

            if(status_code == 200):
                logger.info(f"Successfully wrote the secret")
            else:
                raise Exception(f"Status code is {status_code} while writing data to namespace {namespace}")

        else:
            raise Exception(f"Status code is {status_code} while reading data from namespace {namespace}")

    except Exception as e:
        logger.error(f"Error while writing the secret from namespace {namespace} - {e}")

#Main Program
aws_access_key_id = ""
aws_secret_access_key = ""
aws_region = "ap-southeast-1"
namespace = "prod/databases/dbserver1"
secret = '{"book":"potter","film":"bell"}' #Make sure secret value is hardcoded within single quotes and key/value in double quotes

try:
    logger.info(f"Script Started")
    session= boto3.client('secretsmanager', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key,region_name=aws_region)

    write_secret(session,namespace,secret)
    
except Exception as e:
    logger.error(f"Error in main program : {e}")
