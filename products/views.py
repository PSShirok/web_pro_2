from django.shortcuts import render

from products.models import Product
from django.views.generic import ListView


class HomeListView(ListView):
    model = Product


class ContactListView(ListView):
    model = Product
    template_name = 'products/contact_list.html'

