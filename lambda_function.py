import json
import boto3

def lambda_handler(event, context):
    glue = boto3.client('glue')
    
    try:
        # JDBC URL for Redshift
        redshift_jdbc = "jdbc:redshift://redshift-glue-endpoint-endpoint-eyijoybjkinrns2znbau.646047875925.us-east-2.redshift-serverless.amazonaws.com:5439/dev"

        # Start Glue job
        response = glue.start_job_run(
            JobName='ecommerce-etl-job',
            Arguments={
                '--REDSHIFT_JDBC_URL': redshift_jdbc
            }
        )
        
        return {
            'statusCode': 200,
            'body': json.dumps(f'Glue job started: {response["JobRunId"]}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
