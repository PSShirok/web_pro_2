from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from products.models import Product, Category

@admin.register(Product)
class Product_admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category', )
    list_filter = ('category',)
    search_fields = ('name', 'text',)


@admin.register(Category)
class Category_admin(admin.ModelAdmin):
    list_display = ('id', 'name', )

