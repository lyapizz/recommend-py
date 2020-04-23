from django.contrib import admin

from .actions.films.omdp import importFilmOMDB
from .models import Film, Ratings


class FilmAdmin(admin.ModelAdmin):
    # ...
    fields = ('imdbID',)
    list_display = ('Title', 'Year', 'Poster', 'imdbID')
    search_fields = ['Title', 'imdbID']

    def save_model(self, request, obj, form, change):
        imdbID = form.cleaned_data.get('imdbID')
        importFilmOMDB(imdbID)


admin.site.register(Film, FilmAdmin)
admin.site.register(Ratings)
