from django.urls import path
from . import views

app_name='accounts'
urlpatterns = [
    path('register/',views.UserRegisterView.as_view(),name='register-page'),
    path('login/',views.UserLoginView.as_view(),name='login-page'),
    path('logout/',views.UserLogoutView.as_view(),name='logout-page'),
    path('verify_user/',views.UserVerifyCodeView.as_view(),name='verify-code'),
]
