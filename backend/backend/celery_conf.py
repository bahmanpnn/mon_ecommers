from celery import Celery
from datetime import timedelta
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','backend.settings')

celery_app=Celery('backend') #celery app name must be project name
celery_app.autodiscover_tasks()

celery_app.conf.broker_url='amqp://' #its for localhost.for server it must change.'amqp://guest:guest@localhost:port'
# celery_app.conf.broker_url='amqp://guest:guest@localhost:15672' #its for localhost.for server it must change.'amqp://guest:guest@localhost:port'
celery_app.conf.result_backend='rpc://'
celery_app.conf.task_serializer='json' #defaul mode
celery_app.conf.result_serializer='pickle' #defaul mode is json but for more info set pickle,json is better
celery_app.conf.accept_content=['json','pickle']
celery_app.conf.result_expires=timedelta(days=1)
celery_app.conf.task_always_eager=False #it means that user must waiting for completing task or not
# if task are small and ez its good to set 4 but if its big task and need more source,must set 1
celery_app.conf.worker_prefetch_multiplier=4 
