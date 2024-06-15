from django.shortcuts import render
from django.views import View
from .tasks import all_bucket_objects_task
# Create your views here.

def home_page(request):
    return render(request,'home/homepage.html')

class BucketView(View):
    template_name='home/bucket.html'

    def get(self,request):
        objects=all_bucket_objects_task()
        print('='*100)
        print(objects)
        return render(request,self.template_name,{
            'objects':objects
        })


