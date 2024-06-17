import boto3
from django.conf import settings


class Bucket:
    """
        CDN Bucket Manager

        init method creates connection with arvan cloud bucket
        
        get_objects method get all objects from arvan cloud bucket in dic==>tasks.py==>celery==>bucket view
        
        delete_object method is for deleting one object from arvan cloud bucket and it use in delete obj view
         

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
        
    def delete_object(self,key):
        self.connection_bucket.delete_object(Bucket=settings.AWS_STORAGE_BUCKET_NAME,Key=key)
        return True
    
    def download_object(self,key):
        with open(settings.AWS_LOCAL_STORAGE+key,'wb') as f:
            self.connection_bucket.download_fileobj(settings.AWS_STORAGE_BUCKET_NAME,key,f)

    

bucket_instance=Bucket()

