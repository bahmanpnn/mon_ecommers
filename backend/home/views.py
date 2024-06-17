from django.shortcuts import render,redirect
from django.views import View
from . import tasks as home_tasks
from django.contrib import messages

def home_page(request):
    return render(request,'home/homepage.html')

class BucketView(View):
    template_name='home/bucket.html'

    def get(self,request):
        objects=home_tasks.all_bucket_objects_task()
        # print('='*100)
        # print(objects)
        return render(request,self.template_name,{
            'objects':objects
        })


class DeleteObjectView(View):
    def get(self,request,key):
        home_tasks.delete_object_task.delay(key)
        messages.success(request,'your object will be delete soon',extra_tags='info')
        return redirect('home:bucket')

class DownloadObjectView(View):
    def get(self,request,key):
        home_tasks.download_object_task.delay(key)
        messages.success(request,'your object will be delete soon',extra_tags='info')
        return redirect('home:bucket')