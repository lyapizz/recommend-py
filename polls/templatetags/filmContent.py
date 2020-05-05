from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.template import loader

register = template.Library()


@register.simple_tag(takes_context=True)
def filmContent(context, film):
    request = context.get('request')
    prevFilmId = None
    nextFilmId = None
    if context.get('film') == film:
        if context.get('prevFilm'):
            prevFilmId = context.get('prevFilm').id
        if context.get('nextFilm'):
            nextFilmId = context.get('nextFilm').id

    return loader.get_template('polls/filmContent.html').render(
        {'film': film, 'prevFilmId': prevFilmId, 'nextFilmId': nextFilmId}, request=request)


@register.simple_tag
def settings_value(name):
    return getattr(settings, name, "")
