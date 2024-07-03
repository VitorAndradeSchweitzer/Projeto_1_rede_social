from django import template

register = template.Library()

@register.filter(name='char_count')

def char_count(value):
    if not isinstance(value, str):
        return 0
    return len(value)