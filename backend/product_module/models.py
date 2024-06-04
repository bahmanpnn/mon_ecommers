from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=127)
    slug=models.SlugField(unique=True,db_index=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'


class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='product_category')
    name=models.CharField(max_length=255)
    slug=models.SlugField(unique=True,db_index=True)
    image=models.ImageField(upload_to='products/%Y%M%D')
    description=models.TextField()
    # if we have national website or use dollar and euro,... need Decimal price ==>123.45
    # price=models.DecimalField(max_digits=7,decimal_places=2)
    price=models.IntegerField() 
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)
    is_active=models.BooleanField(default=True)

    class Meta:
        ordering=('created_date','name')

    def __str__(self):
        return self.name
    
    
    

    
    
