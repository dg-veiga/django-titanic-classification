from django import template

import json

register = template.Library()

@register.filter(name='tojson', is_safe=True)
def tojson(value):
    return json.dumps(value)