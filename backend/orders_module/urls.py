from django.urls import path
from . import views

app_name='orders'
urlpatterns = [
    path('basket/',views.BasketView.as_view(),name='basket'),
    path('basket/add/<int:product_id>',views.BasketAddView.as_view(),name='basket-add'),
]
