from django.urls import path,include
from . import views

app_name="home"

bucket_urls=[
    path('',views.BucketView.as_view(),name='bucket'),
    path('delete_object/<key>/',views.DeleteObjectView.as_view(),name='bucket-delete-object'),
]

urlpatterns = [
    path('',views.home_page,name='home-page'),
    path('bucket/',include(bucket_urls)),
]
