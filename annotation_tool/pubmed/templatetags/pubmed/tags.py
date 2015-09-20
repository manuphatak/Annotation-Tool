# Python Libraries
import re

# Django Packages
from django import template

register = template.Library()

_re_camel_humps = re.compile('([a-z])([A-Z0-9])')
_to_kabob = r'\1-\2'


@register.simple_tag
def css_class(*args, **kwargs):
    more_args = tuple(_re_camel_humps.sub(_to_kabob, key).lower() for key, value in kwargs.items() if value)
    css_classes = ' '.join(str(arg) for arg in set(args + more_args) if arg) or ' '
    return ' class="%s" ' % css_classes if css_classes else ' '


@register.simple_tag(takes_context=True)
def field_required(context):
    return ' <span class="asteriskField">*</span>' if context['field'].field.required else ''
