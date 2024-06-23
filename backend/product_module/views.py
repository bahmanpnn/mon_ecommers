from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Product,Category


class ProductsView(View):
    template_name='product_module/products.html'

    def get(self,request,category_slug=None):
        products=Product.objects.filter(is_active=True).order_by('-created_date')
        categories=Category.objects.filter(is_sub=False)

        if category_slug:
            category=Category.objects.get(slug=category_slug)
            products=products.filter(category=category)

        return render(request,self.template_name,{
            'products':products,
            'categories':categories
        })
    

class ProductDetailView(View):
    template_name='product_module/product_detail.html'

    def get(self,request,slug):
        target_product=get_object_or_404(Product,slug=slug)
        # target_product=Product.objects.get(slug=slug) #get (object,or return None)
        return render(request,self.template_name,{
            'product':target_product
        })
    
    # def get(self,request,slug):
    #     # target_product=get_object_or_404(Product,slug=slug)
    #     target_product=Product.objects.get(slug=slug) #get (object,or return None)
        
    #     if target_product is not None:
    #         return render(request,self.template_name,{
    #             'product':target_product
    #         })
        
    
    def post(self,request):
        pass
