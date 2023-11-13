from django.urls import path

from products.views import ContactListView, HomeListView, ProductCreateView, ProductUpdateView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('contact_list/', ContactListView.as_view(), name='contact_list'),
    path('', HomeListView.as_view(), name='home'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),

]
