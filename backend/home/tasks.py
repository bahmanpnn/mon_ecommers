from bucket import bucket_instance

# TODO:must be async
def all_bucket_objects_task():
    result=bucket_instance.get_objects()
    return result

