from django.urls import path

from products.views import contacts_index, home_index, page_index, model_sample, about_product
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('contacts/', contacts_index, name='contacts'),
    path('', home_index, name='home'),
    path('product/', page_index, name='product'),
    path('model_sample/', model_sample, name='model_sample'),
    path('<int:pk>/about_product/', about_product, name='about_product'),

]
