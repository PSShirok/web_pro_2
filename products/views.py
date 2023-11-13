from django.shortcuts import render
from django.urls import reverse_lazy

from products.forms import ProductForm
from products.models import Product
from django.views.generic import ListView, CreateView, UpdateView


class HomeListView(ListView):
    model = Product


class ContactListView(ListView):
    model = Product
    template_name = 'products/contact_list.html'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:home')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:home')