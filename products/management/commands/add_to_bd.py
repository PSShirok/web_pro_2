from django.core.management import BaseCommand

from products.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        Product.objects.all().delete()
        Category.objects.all().delete()

        category_list = [
            {'id': 1, 'name': 'Овощи', 'text': 'натурпродукт'},
            {'id': 2, 'name': 'Фрукты', 'text': 'натурпродукт'}
        ]

        for st in category_list:
            Category.objects.create(**st)