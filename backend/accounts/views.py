from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from random import randint
from utils import send_otp_code
from .forms import UserRegisterForm,VerifycodeForm
from .models import OtpCode,User

class UserRegisterView(View):
    form_class=UserRegisterForm
    template_name='accounts/register.html'
    
    def get(self,request):
         
        return render(request,self.template_name,{
            'form':self.form_class()
        })

    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            random_code=randint(1000,9999)
            
            # send code and phone number to function in utils to use them and sms code to user
            send_otp_code(cd['phone_number'],random_code) 
            #sms code to phone number
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'],code=random_code) 

            #save data in sessions to use them again if code is true and register user with them
            request.session['user_registeration_info']={
                'phone_number':cd['phone_number'],
                'email':cd['email'],
                'fullname':cd['fullname'],
                'password':cd['password'],
            }

            messages.success(request,'we sent you a code; please check your phone to fill form for registration',extra_tags='success')
            return redirect('accounts:verify-code')
        
        # return render('accounts:register-page') ==>if form is not valid we need to show erros so,
        # its not correct to redirect user to this page again without form!!!so use render to pass form
        return render(request,self.template_name,{
            'form':self.form_class(request.POST)
        })
    

class UserVerifyCodeView(View):
    template_name='accounts/verify_code.html'
    form_class=VerifycodeForm

    def get(self,request):
        return render(request,self.template_name,{
            'form':self.form_class()
        })

    def post(self,request):
        user_session=request.session['user_registeration_info']
        code_instance=OtpCode.objects.get(phone_number=user_session['phone_number'])

        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user_code=cd['code']
            if user_code ==code_instance.code:
                User.objects.create_user(phone_number=user_session['phone_number'],
                                         email=user_session['email'],
                                         fullname=user_session['fullname'],
                                         password=user_session['password']
                                         )
                code_instance.delete()
                messages.success(request,'you registered succussfully!! now login please ;)) ')
                return redirect('home:home-page')
            else:
                messages.error(request,'this code is wrong.if you fill correctly numbers its expired.\
                               please register again',extra_tags='danger')
                return redirect('accounts:verify-code')
        return redirect('accounts:verify-code')
            