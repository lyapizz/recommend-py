from __future__ import unicode_literals

from django import template
from django.template import loader

register = template.Library()


@register.simple_tag(takes_context=True)
def filmContent(context, film):
    request = context.get('request')
    return loader.get_template('polls/filmContent.html').render({
        'film': film
    }, request=request)
