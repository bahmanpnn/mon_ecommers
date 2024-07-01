from random import randint
from utils import send_otp_code
from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from orders_module.models import Order
from .forms import UserRegisterForm,VerifycodeForm,LoginForm,ProfileForm
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


class UserLoginView(View):
    template_name='accounts/login.html'
    form_class=LoginForm

    def get(self,request):
        return render(request,self.template_name,{
            'form':self.form_class()
        })
    
    def post(self,request):
        form=self.form_class(request.POST)

        if form.is_valid():
            cd=form.cleaned_data

            check_phone_number=User.objects.filter(phone_number=cd['email_or_phone_number']).exists()
            if check_phone_number:
                user=authenticate(request,phone_number=cd['email_or_phone_number'],password=cd['password'])
                if user is not None:
                    login(request,user)
                    messages.success(request,'you logged in successfully!!',extra_tags='success')
                    return redirect('home:home-page')

            check_email=User.objects.filter(email=cd['email_or_phone_number']).exists()
            if check_email:
                check_user=User.objects.get(email=cd['email_or_phone_number'])
                check_user_password=check_user.check_password(cd['password'])
                
                if check_user_password:
                    login(request,check_user)
                    messages.success(request,'you logged in successfully!!',extra_tags='success')
                    return redirect('home:home-page')
                else:
                    messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
            else:
                messages.error(request,'password or email-phone_number is wrong!! ',extra_tags='danger')
        
        return render(request,self.template_name,{
            'form':form
        })
                    
            
class UserLogoutView(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you logged out successfully!!',extra_tags='success')
        return redirect('home:home-page')


class UserProfileView(LoginRequiredMixin,View):
    form_class=ProfileForm
    template_name='accounts/profile.html'
    
    def get(self,request):
        
        return render(request,self.template_name,{
            'form':self.form_class(instance=request.user)
        })

    def post(self,request):
        # TODO: check email and phone to dont exist in database and used before except this user
        # TODO: after checking send otp code for phone number or email for email if changed 
        form=self.form_class(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'profile updated successfully',extra_tags='success')
            return redirect('accounts:user-profile')


class UserReceiptView(LoginRequiredMixin,View):
    template_name='accounts/receipts.html'

    def get(self,request):
        receipts=Order.objects.filter(user=request.user,is_paid=True)

        return render(request,self.template_name,{
            'receipts':receipts
        })


