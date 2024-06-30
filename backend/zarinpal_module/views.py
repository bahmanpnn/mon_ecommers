from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from orders_module.models import Order
import requests
import json


# sandbox merchant 
if settings.SANDBOX:
    sandbox = 'sandbox'
else:
    sandbox = 'www'


ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 1000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
phone = ''  # Optional

# Important: need to edit for realy server.
CallbackURL = 'http://127.0.0.1:8000/checkout/pay/verify'
# CallbackURL = 'http://127.0.0.1:8000/checkout/verify/'
# CallbackURL = 'http://127.0.0.1:8000/{% url "zarinpal:verify" %}'


class OrderPayView(LoginRequiredMixin,View):
    def get(self,request,order_id):
        order=Order.objects.get(id=order_id)
        request.session['order_pay']={
            'order_id':order.id,
        }

        print(order.user.phone_number)
        print(request.user.phone_number)

        data = {
            "MerchantID": settings.MERCHANT,
            # "Amount": order.get_total_price(),
            # "Amount": order.get_total_price()*10 #change toman to rial,
            "Amount": amount,
            "Description": description,
            "Phone": request.user.phone_number,
            # "Phone": phone,
            "CallbackURL": CallbackURL,
        }
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        try:
            response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

            if response.status_code == 200:
                response = response.json()
                if response['Status'] == 100:
                    return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
                else:
                    return {'status': False, 'code': str(response['Status'])}
            return response
        
        except requests.exceptions.Timeout:
            return {'status': False, 'code': 'timeout'}
        except requests.exceptions.ConnectionError:
            return {'status': False, 'code': 'connection error'}


class OrderVerifyView(LoginRequiredMixin,View):
    def get(self,request):
    # def get(self,request,authority=None):
    # def get(self,authority,request=None):
        
        order_id=request.session['order_pay']['order_id']
        order=Order.objects.get(id=int(order_id))


        data = {
        "MerchantID": settings.MERCHANT,
        # "Amount": order.get_total_price()*10,
        # "Amount": order.get_total_price(),
        "Amount": amount,
        "Authority": 'authority',
        # "Authority": request.GET.get['authority'],
        # "Authority": authority,
        }
        
        data = json.dumps(data)
        # set content length by data
        headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
        response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'RefID': response['RefID']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response


def send_request(request):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": phone,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)

        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return {'status': True, 'url': ZP_API_STARTPAY + str(response['Authority']), 'authority': response['Authority']}
            else:
                return {'status': False, 'code': str(response['Status'])}
        return response
    
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(authority):
    data = {
        "MerchantID": settings.MERCHANT,
        "Amount": amount,
        "Authority": authority,
    }
    data = json.dumps(data)
    # set content length by data
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)

    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100:
            return {'status': True, 'RefID': response['RefID']}
        else:
            return {'status': False, 'code': str(response['Status'])}
    return response