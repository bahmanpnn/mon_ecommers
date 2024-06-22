from kavenegar import *
from django.contrib.auth.mixins import UserPassesTestMixin


def send_otp_code(phone_number,code):
    try:
        my_api=''
        api = KavenegarAPI(my_api)
        params = {
            'sender': '', #optional
            'receptor': phone_number,#multiple mobile number, split by comma
            'message': f':کد تایید شما{code}'
        } 
        response = api.sms_send(params)
        print(response)
    except APIException as e: 
        print(e)
        # print(err.decode('utf-8'))
    except HTTPException as e: 
        print(e)

        
# if you faced with error and error was persian you must decode it to utf-8 ==>

# err=b'\xd8\xa7\xd8\xb1\xd8\xb3\xd8\xa7\xd9\x84 \xda\xa9\xd9\x86\xd9\x86\xd8\xaf\xd9\x87 \xd9\x86\xd8\xa7\xd9\x85\xd8\xb9\xd8\xaa\xd8\xa8\xd8\xb1 \xd8\xa7\xd8\xb3\xd8\xaa'
# print(err.decode('utf-8'))

#------------------------------------------------------------------------------
# otp in doc
# from kavenegar import *
# try:
#     api = KavenegarAPI('Your APIKey', timeout=20)
#     params = {
#         'receptor': '',
#         'template': '',
#         'token': '',
#         'type': 'sms',#sms vs call
#     }   
#   response = api.verify_lookup(params)
#   print(response)
# except APIException as e: 
#   print(e)
# except HTTPException as e: 
#   print(e)



class IsUserAdminMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_admin
