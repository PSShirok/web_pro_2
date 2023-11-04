from django import template

from django.conf import settings


register = template.Library()


@register.filter()
def mediapath(image):
    if image:
        media_url = settings.MEDIA_URL
        return f'{media_url}/{image}'
    return f'/media/products/default_img.jpg'
