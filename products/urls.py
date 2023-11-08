from django.urls import path

from products.views import ContactListView, HomeListView
from products.apps import ProductsConfig

app_name = ProductsConfig.name

urlpatterns = [
    path('contact_list/', ContactListView.as_view(), name='contact_list'),
    path('', HomeListView.as_view(), name='home'),

]
