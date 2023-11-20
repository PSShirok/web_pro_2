import random

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
    is_active = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def verify_key(self):
        user_key = ''.join([str(random.randint(0, 9)) for _ in range(8)])

        return user_key
