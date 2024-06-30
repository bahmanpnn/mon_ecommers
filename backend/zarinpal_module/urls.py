from django.urls import path
from . import views


app_name='zarinpal'
urlpatterns = [
    path('request/', views.send_request, name='request'),
    path('verify/', views.verify , name='verify'),
    path('pay/<int:order_id>/',views.OrderPayView.as_view(),name='order-pay'),
    path('pay/verify',views.OrderPayView.as_view(),name='order-verify'),
]