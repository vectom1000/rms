from django import template

register = template.Library()


@register.filter
def gib_photo_string(value, arg):
    """Removes all values of arg from the given string"""
    return value