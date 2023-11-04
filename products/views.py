from django.shortcuts import render

from products.models import Product


# Create your views here.
def contacts_index(request):
    return render(request, 'products/contacts.html')


def home_index(request):
    return render(request, 'products/home.html')


def model_sample(request):
    return render(request, 'products/model_sample.html')


def page_index(request):
    product_list = Product.objects.all()
    content = {
        'object_list': product_list
    }
    return render(request, 'products/index.html', content)


def about_product(request, pk):
    product_category = Product.objects.get(pk=pk)
    product_list = Product.objects.filter(category_id=pk)
    content = {
        'object_list': product_list
    }
    return render(request, 'products/index.html', content)
