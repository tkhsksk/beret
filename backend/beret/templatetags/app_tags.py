import os
import json

from django.conf import settings
from django import template

register = template.Library()

@register.inclusion_tag('parts/menu.html', takes_context=True)
def render_category_links(context):
    path = os.path.join(settings.BASE_DIR.parent, 'beret/static/aside.json')
    json_open = open(path).read()
    datas = json.loads(json_open)

    request = context['request']

    return {
        'aside_menus': datas,
        'request':request
    }