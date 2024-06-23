from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('',views.ProductsView.as_view(),name='products'),
    path('category/<slug:category_slug>/',views.ProductsView.as_view(),name='category'),
    path('<slug:slug>',views.ProductDetailView.as_view(),name='product-detail'),
]
