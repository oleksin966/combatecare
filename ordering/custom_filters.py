from django import template

register = template.Library()

@register.filter
def replace_decimal_separator(value):
    return str(value).replace(',', '.')

