from celery import shared_task
from accounts.models import OtpCode
from datetime import datetime,timedelta
import pytz
       


@shared_task
def remove_all_expired_otp_codes_task():
    expired_time=datetime.now(tz=pytz.timezone('Asia/Tehran'))-timedelta(minutes=2)
    OtpCode.objects.filter(created_date__lt=expired_time).delete()