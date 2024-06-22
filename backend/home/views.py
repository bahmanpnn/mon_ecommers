from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
# from django.contrib.auth.mixins import UserPassesTestMixin
from utils import IsUserAdminMixin
from . import tasks as home_tasks

def home_page(request):
    return render(request,'home/homepage.html')

class BucketView(IsUserAdminMixin,View):
    template_name='home/bucket.html'

    def get(self,request):
        objects=home_tasks.all_bucket_objects_task()
        
        return render(request,self.template_name,{
            'objects':objects
        })
    
# class BucketView(UserPassesTestMixin,View):
#     template_name='home/bucket.html'

#     def get(self,request):
#         objects=home_tasks.all_bucket_objects_task()

#         return render(request,self.template_name,{
#             'objects':objects
#         })
    
#     def test_func(self):
#         return self.request.user.is_authenticated and self.request.user.is_admin


class DeleteObjectView(IsUserAdminMixin,View):
    def get(self,request,key):
        home_tasks.delete_object_task.delay(key)
        messages.success(request,'your object will be delete soon',extra_tags='info')
        return redirect('home:bucket')

class DownloadObjectView(IsUserAdminMixin,View):
    def get(self,request,key):
        home_tasks.download_object_task.delay(key)
        messages.success(request,'your object will be delete soon',extra_tags='info')
        return redirect('home:bucket')
    