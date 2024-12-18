import boto3
import os

s3 = boto3.client('s3', endpoint_url='http://localhost:4566')

def lambda_handler(event, context):
    for record in event['Records']:
        source_bucket = record['s3']['bucket']['name']
        source_key = record['s3']['object']['key']
        destination_bucket = 's3-finish'

        try:
            copy_source = {'Bucket': source_bucket, 'Key': source_key}
            s3.copy_object(
                Bucket=destination_bucket,
                Key=source_key,
                CopySource=copy_source
            )
            print("Файл", source_key, "успішно скопійовано з", source_bucket, "до", destination_bucket)
        except Exception as e:
            print("Помилка копіювання файлу", source_key, ":", str(e))