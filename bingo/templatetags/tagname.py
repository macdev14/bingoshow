# app/templatetags/tagname.py

from django import template
from random import randint, choice

register = template.Library()

@register.filter
def get_range(value):
    return range(value)

@register.filter
def bingoletter_load(value):

    b = ['B', 'I', 'N', 'G', 'O']
    j = choice(b) + str(randint(1,75))
    print(j)
    return j