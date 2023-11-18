from django.db import models

# Create your models here.
from django.db import models

from users.models import User

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
    image = models.ImageField(upload_to='products/', **NULLBALE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    create_date = models.DateField(auto_now_add=True)
    change_date = models.DateField(auto_now=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, **NULLBALE)

    def __str__(self):
        return (f'{self.name} \n'
                f'{self.text}')


class Version(models.Model):

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    version_num = models.IntegerField(**NULLBALE)
    version_name = models.CharField(max_length=50, **NULLBALE)
    ver_is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.version_num} {self.version_name}'

