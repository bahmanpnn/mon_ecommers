from django.urls import path,include
from . import views

app_name='orders'
basket_urls=[
    path('',views.BasketView.as_view(),name='basket'),
    path('add/<int:product_id>/',views.BasketAddView.as_view(),name='basket-add'),
    path('remove/<int:product_id>/',views.BasketRemoveView.as_view(),name='basket_remove'),
]

urlpatterns = [
    path('basket/',include(basket_urls)),
    #orders
    path('order_create/',views.OrderCreateView.as_view(),name='order-create'),
    path('order_detail/<int:order_id>/',views.OrderDetailView.as_view(),name='order-detail'),
    path('coupon_apply/<int:order_id>/',views.CouponApplyView.as_view(),name='coupon-apply'),
]
