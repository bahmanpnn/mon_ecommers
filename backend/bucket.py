import boto3
from django.conf import settings


class Bucket:
    """
        CDN Bucket Manager

        init method creates connection
    """
    def __init__(self):
        session=boto3.session.Session()
        self.connection_bucket=session.client(
            service_name=settings.AWS_SEVICE_NAME,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )

