# Create a file named 'custom_filters.py' in your Django app

# custom_filters.py
from django import template

register = template.Library()

@register.filter
def break_after_first(value):
    if value:
        # Return only the first item in the list
        return [value[0]]
    return value
