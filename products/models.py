from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
NULLBALE = {'blank': True, 'null': True}


class Category (models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField(**NULLBALE)

    def __str__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=50)
    text = models.TextField(**NULLBALE)
    # image = models.ImageField(**NULLBALE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


