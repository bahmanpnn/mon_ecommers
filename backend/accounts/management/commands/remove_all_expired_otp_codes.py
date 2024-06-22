from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime,timedelta


class Command(BaseCommand):
    """
        this class removes all expired otp codes with django-admin command in terminal
        like python manage.py runserver or django-admin runserver ==>
        python manage.py remove_all_expired_otp_codes

        handle method overrided and otp codes delete with this method and then write a message on terminal
    """

    help="remove all expired otp codes"

    def handle(self, *args, **options):
        expired_time=datetime.now()-timedelta(minutes=2)
        OtpCode.objects.filter(created_date__lt=expired_time).delete()

        self.stdout.write(self.style.SUCCESS('otp codes removed successfully!!'))
        # self.stdout.write('otp codes removed successfully!!')