from django.contrib import admin
from .models import Order,OrderItem


class OrderItemInline(admin.TabularInline):
    model=OrderItem
    raw_id_fields=('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    '''
        this is main admin page that use OrderModel and 
        after data of Order model we can see Order Item model like table and
        default has 3 item in table that every item is one order item
    '''
    list_display=('id','user','updated_date','is_paid')
    list_filter=('is_paid',)
    inlines=(OrderItemInline,) 


# admin.site.register(Order,OrderAdmin)