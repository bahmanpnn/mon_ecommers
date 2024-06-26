from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls',namespace='home')),
    path('accounts/',include('accounts.urls',namespace='accounts')),
    path('orders/',include('orders_module.urls',namespace='orders')),
    path('products/',include('product_module.urls',namespace='products')),
    path('checkout/',include('zarinpal_module.urls',namespace='zarinpal')),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # this paths are just for devopling mode,
# everytime you want to use server must delete static path and dont need media roots and urls
