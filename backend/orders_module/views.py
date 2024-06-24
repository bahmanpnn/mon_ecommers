from django.shortcuts import render
from django.views import View

class BasketView(View):
    template_name="orders_module/basket.html"

    def get(self,request):
        return render(request,self.template_name)
    
class BasketAddView(View):
    def post(self,request,product_id):
        pass