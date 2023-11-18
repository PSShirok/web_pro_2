from django.contrib.auth.models import AbstractUser
from django.db import models


from blog.models import NULLBALE


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    avatar = models.ImageField(upload_to='users/', **NULLBALE)
    phone = models.CharField(max_length=30, **NULLBALE)
    country = models.CharField(max_length=30, **NULLBALE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
