import boto3

s3_endpoint_url = 'https://obs.ru-moscow-1.hc.sbercloud.ru'
key_id = 'E6Q8RYDZNKQCBVMCQZXE'
access_key = 'UqbuPnODO9STNrCmqc76rj9Iq4LMlqwp3Fi0Gc1Q'
bucket_name = 'hackathon-ecs-53'


def upload_file(file_path):
    session = boto3.session.Session()

    client = session.client (
       service_name="s3",
       endpoint_url=s3_endpoint_url,
       aws_access_key_id=key_id,
       aws_secret_access_key=access_key,
       use_ssl=False,
       verify=False,
    )

    client.upload_file(file_path, bucket_name, 'test_video')
    print('Video upload complete')
