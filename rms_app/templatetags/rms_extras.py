from django import template
from django.conf.urls.static import static

register = template.Library()


@register.filter
def gib_photo_string(value):
    """Removes all values of arg from the given string"""
    path = '/static/rms_app/photos/{0}.jpg'.format(value)
    return path
