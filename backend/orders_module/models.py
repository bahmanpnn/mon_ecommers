'''
    this models using when user wants to pay and models get their datas from session that
    filled before with basket session.

    we can get user with 3 ways==>
    1- from django.contrib.auth import User -->if changed user model --> from accounts.models import User
    2- from django.conf import settings --> settings.AUTH_USER_MODEL
    3- from django.contrib.auth import get_user_model

'''

from django.db import models
from django.contrib.auth import get_user_model
from product_module.models import Product
from django.core.validators import MinValueValidator,MaxValueValidator


User=get_user_model()

class Order(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='orders')
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_paid=models.BooleanField(default=False)
    discount=models.PositiveIntegerField(blank=True,null=True,default=None)

    class Meta:
        ordering=('is_paid','-created_date','-updated_date')

    def __str__(self):
        return f'{self.user} - {self.is_paid}'
    
    def get_total_price(self):
        total= sum(item.get_cost() for item in self.order_items.all())
        if self.discount:
            discount_price=(self.discount / 100 )*total
            return int(total-discount_price)
        return total

class OrderItem(models.Model):
    order=models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product=models.ForeignKey(Product,on_delete=models.PROTECT)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity
    
class Coupon(models.Model):
    code=models.CharField(max_length=15,unique=True)
    valid_from=models.DateTimeField()
    valid_to=models.DateTimeField()
    discount=models.PositiveIntegerField(validators=[MinValueValidator(0),MaxValueValidator(90)])
    is_active=models.BooleanField(default=False)

    def __str__(self):
        return self.code
