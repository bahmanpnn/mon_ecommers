from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from product_module.models import Product
from .forms import AddBasketForm
from .basket import Basket
from django.contrib import messages

class BasketView(View):
    template_name="orders_module/basket.html"

    def get(self,request):
        return render(request,self.template_name)
    
class BasketAddView(View):
    '''
        post method comes from product detail view form that has a integer field,
        with basket.py and sessions we can add a product to basket and
        show them in table of basket.html and it uses in BasketView. 
    '''
    def post(self,request,product_id):
        basket=Basket(request)
        product=get_object_or_404(Product,id=product_id)
        form=AddBasketForm(request.POST)

        if form.is_valid():
            basket.add(product,form.cleaned_data['quantity'])

        messages.success(request,'product added to basket successfully!!',extra_tags='success')
        return redirect('product_module:products')
        # return redirect('product_module:product-detail',product.slug)