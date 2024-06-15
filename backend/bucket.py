import boto3
from django.conf import settings


class Bucket:
    """
        CDN Bucket Manager

        init method creates connection with arvan cloud bucket

        NOTE:
            None of this methods are async.you must use public interface in tasks.py modules instead!!
    """

    def __init__(self):
        session=boto3.session.Session()
        self.connection_bucket=session.client(
            service_name=settings.AWS_SEVICE_NAME,
            aws_access_key_id=settings.AWS_S3_ACCESS_KEY_ID,
            aws_secret_access_key=settings.AWS_S3_SECRET_ACCESS_KEY,
            endpoint_url=settings.AWS_S3_ENDPOINT_URL,
        )
    
    def get_objects(self):
        result=self.connection_bucket.list_objects_v2(Bucket=settings.AWS_STORAGE_BUCKET_NAME)
        if result['KeyCount']:
            return result['Contents']
        else:
            return None
    

bucket_instance=Bucket()

