from django import template

register = template.Library()

@register.filter
def getattribute(value, arg):
    """Gets an attribute of an object dynamically from a string name"""
    try:
        return getattr(value, str(arg))
    except AttributeError:
        return None

@register.filter
def get_form_field(field_name, form):
    """Gets a form field by its name"""
    try:
        return form[field_name]
    except KeyError:
        return None