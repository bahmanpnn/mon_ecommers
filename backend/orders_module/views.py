from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from product_module.models import Product
from .forms import AddBasketForm,CouponApplyForm
from .basket import Basket
from .models import Order,OrderItem,Coupon
import datetime

class BasketView(LoginRequiredMixin,View):
    '''
        Todo:set session time for few hours
        because if price change in database and admin panel; session show last price not new price!!
        or if project has product count, session cant help user to understand product sold out and
        there is any of that!!
    '''
    template_name="orders_module/basket.html"

    def get(self,request):
        basket=Basket(request)

        # print('='*90)
        # print(basket.basket) # basket(classname).basket(variable name)
        # print(basket.__dict__)
        # print(len(basket.basket))
        # print(bool(basket.basket))

        return render(request,self.template_name,{
            'basket':basket,
            'check_basket':bool(basket.basket)
        })


class BasketAddView(LoginRequiredMixin,View):
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
        return redirect('products:products')
        # return redirect('product_module:product-detail',product.slug)


class BasketRemoveView(LoginRequiredMixin,View):

    def get(self,request,product_id):
        basket=Basket(request)
        product=get_object_or_404(Product,id=product_id)
        if product:
            basket.remove_product(product)
            messages.success(request,'product removed successfully',extra_tags='success')
            return redirect('orders:basket')


class OrderDetailView(LoginRequiredMixin,View):
    template_name='orders_module/checkout.html'
    form_class=CouponApplyForm

    def get(self,request,order_id):
        order=get_object_or_404(Order,id=order_id)

        return render(request,self.template_name,{
            'order':order,
            'form':self.form_class
        })
    
    
    
class OrderCreateView(LoginRequiredMixin,View):
    def get(self,request):
        basket=Basket(request)
        order=Order.objects.create(user=request.user)
        for item in basket:
            OrderItem.objects.create(order=order,product=item['product'],price=item['price'],quantity=item['quantity'])
        # basket.clear() #it clears items of basket and suppose to order paid!!
        return redirect('orders:order-detail',order.id)

class CouponApplyView(LoginRequiredMixin,View):
    form_class=CouponApplyForm

    def post(self,request,order_id):
        now=datetime.datetime.now()
        form=self.form_class(request.POST)

        if form.is_valid():
            code=form.cleaned_data['code']
            try:
                coupon=Coupon.objects.get(code__exact=code,valid_from__lte=now,valid_to__gte=now,is_active=True)

            except Coupon.DoesNotExist:
                messages.error(request,'this coupon does not exists or maybe expired!!',extra_tags='danger')
                return redirect('orders:order-detail',order_id)
            
            order=Order.objects.get(id=order_id)
            order.discount=coupon.discount
            order.save()
            messages.success(request,'coupon added successfully',extra_tags='success')
        return redirect('orders:order-detail',order_id)