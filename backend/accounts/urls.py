from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register-page'),
    path('verify_user/',views.UserVerifyCodeView.as_view(),name='verify-code'),
]
