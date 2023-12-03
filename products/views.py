from django.forms import inlineformset_factory, formset_factory, modelformset_factory, modelform_factory
from django.shortcuts import render
from django.urls import reverse_lazy

from products.forms import ProductForm, VersionForm, ModeratorProductForm
from products.models import Product, Version
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group


class HomeListView(LoginRequiredMixin, ListView):
    model = Product


class ContactListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/contact_list.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:home')

    def get_form_class(self):
        if self.request.user.groups.filter(name='moderators').exists():
            return ModeratorProductForm
        else:
            return ProductForm



    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if self.request.user.is_staff:
            VersionFormset = modelform_factory(Product, form=VersionForm)
        else:
            VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = VersionFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = VersionFormset(instance=self.object)
        return context_data


    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user != kwargs['instance'].user_id:
            return self.handle_no_permission()
        return kwargs
