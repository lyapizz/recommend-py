import re

from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _

from .actions.films.omdp import importFilmOMDB
from .models import Film, Ratings


class FilmAdmin(admin.ModelAdmin):
    # ...
    fields = ('imdbUrl',)
    list_display = ('Title', 'Year', 'Poster', 'imdbID')
    search_fields = ['Title', 'imdbID']

    def save_model(self, request, obj, form, change):
        imdbUrl = form.cleaned_data.get('imdbUrl')
        pieces = re.findall('/?(tt[0-9]+)/?', imdbUrl)
        if len(pieces) > 0:
            imdbID = pieces[0]
            importFilmOMDB(imdbID)


class RatingsAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        return super(RatingsAdmin, self).get_queryset(request).select_related('film', 'user')

    def stars(self, obj):
        html = "<span style='display: block; width: {}px; height: 10px; " + \
               "background: url(/static/star-ratings/images/admin_stars.png)'>&nbsp;</span>"
        return format_html(html, obj.score * 10)

    stars.allow_tags = True
    stars.short_description = _('Score')
    list_display = ('__str__', 'stars')
    ordering = ('score',)


admin.site.register(Film, FilmAdmin)
admin.site.register(Ratings, RatingsAdmin)
