from __future__ import unicode_literals

import uuid
from decimal import Decimal

from django import template
from django.template import loader
from django.templatetags.static import static

from polls.models import Ratings
from star_ratings import app_settings, get_star_ratings_rating_model

register = template.Library()


@register.simple_tag(takes_context=True)
def myratings(context, item, icon_height=app_settings.STAR_RATINGS_STAR_HEIGHT,
              icon_width=app_settings.STAR_RATINGS_STAR_WIDTH, read_only=False, template_name=None):
    request = context.get('request')

    if request is None:
        raise Exception(
            'Make sure you have "django.core.context_processors.request" in your templates context processor list')

    rating = get_star_ratings_rating_model().objects.for_instance(item)

    user_rating = Ratings.objects.get_or_create(film=item, user=request.user)[0]
    rating.average = user_rating.score

    user_rating_percentage = 100 * (user_rating.score / Decimal(app_settings.STAR_RATINGS_RANGE))

    stars = [i for i in range(1, app_settings.STAR_RATINGS_RANGE + 1)]

    # We get the template to load here rather than using inclusion_tag so that the
    # template name can be passed as a template parameter
    template_name = template_name or context.get('star_ratings_template_name') or 'star_ratings/widget.html'
    return loader.get_template(template_name).render({
        'rating': rating,
        'request': request,
        'user': request.user,
        'user_rating': user_rating,
        'user_rating_percentage': user_rating_percentage,
        'stars': stars,
        'star_count': app_settings.STAR_RATINGS_RANGE,
        'percentage': 100 * (user_rating.score / Decimal(app_settings.STAR_RATINGS_RANGE)),
        'icon_height': icon_height,
        'icon_width': icon_width,
        'sprite_width': icon_width * 3,
        'sprite_image': static(app_settings.STAR_RATINGS_STAR_SPRITE),
        'id': 'dsr{}'.format(uuid.uuid4().hex),
        'anonymous_ratings': app_settings.STAR_RATINGS_ANONYMOUS,
        'read_only': read_only,
        'editable': not read_only
    }, request=request)
