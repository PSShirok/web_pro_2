from django.db import models

# Create your models here.
NULLBALE = {'blank': True, 'null': True}


class Blogpost(models.Model):

    name = models.CharField(max_length=50)
    slug = models.CharField(max_length=150, **NULLBALE)
    text = models.TextField(**NULLBALE)
    image = models.ImageField(upload_to='blog/', **NULLBALE)
    create_date = models.DateField(auto_now_add=True)
    is_published = models.BooleanField(default=False)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'
