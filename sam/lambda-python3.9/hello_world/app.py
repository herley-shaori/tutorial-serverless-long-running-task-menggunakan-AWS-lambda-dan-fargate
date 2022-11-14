import json
import requests
import boto3
import logging
import string
import random

logging.basicConfig()
logger = logging.getLogger()
logging.getLogger("botocore").setLevel(logging.ERROR)
logger.setLevel(logging.INFO)

client = boto3.client('ecs')
cluster_name = "random-string-cluster"
task_definition = "random-string-task:5"

def randomStringGenerator(size=17, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def lambda_handler(event, context):
    logger.info('Running ECS Task...')
    response = client.run_task(
            cluster=cluster_name,
            launchType = 'FARGATE',
            taskDefinition=task_definition,
            count = 1,
            platformVersion='LATEST',
            
            overrides = { 
                'containerOverrides':[
                    {
                        'name':'random-string-container',
                        'environment':[
                            {
                                'name':'RANDOM_STRING_FROM_LAMBDA',
                                'value':randomStringGenerator()
                            }
                        ]
                    }
                ]
            },
            networkConfiguration={
                'awsvpcConfiguration': {
                    'subnets': [
                        'subnet-ef5439b6'
                    ],
                    'securityGroups': [
                        "sg-bac1acf7",
                    ],
                    'assignPublicIp': 'ENABLED'
                }
            })


    return {
        'statusCode':200,
        'info':'ok!'
    }