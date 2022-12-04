import boto3
s3 = boto3.client(‘s3’)
s3.upload_file(‘dane.txt’,’12344test12345’,’a.txt’)
