from django.urls import path,include
from . import views

app_name="home"
urlpatterns = [
    path('',views.home_page,name='home-page'),
    path('bucket/',views.BucketView.as_view(),name='bucket'),
    # path('bucket/',include(""))
]
