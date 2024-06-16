from bucket import bucket_instance
from celery import shared_task

# TODO:must be async
def all_bucket_objects_task():
    result=bucket_instance.get_objects()
    return result


@shared_task
def delete_object_task(key):
    bucket_instance.delete_object(key)