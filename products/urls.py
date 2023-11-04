from django.urls import path

from products.views import contacts_index, home_index, page_index
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('contacts/', contacts_index, name='contacts'),
    path('', home_index, name='home'),
    path('product/', page_index, name='product'),



]
