from django import template
from django.template.defaultfilters import register

# two ways of registering the filters:
# 1) use the decorator
# 2) do it with the commented code at lines 7 and 22
# register = template.Library()


@register.filter(name='cut')
# custom filter
def cut(value, arg):
    """
    This cuts out all values of arg from the string
    :param value:
    :param arg:
    :return:
    """
    return value.replace(arg, '')


# register.filter(name='cut', filter_func=cut)