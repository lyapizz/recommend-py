from django.contrib import admin

from .models import Film


class FilmAdmin(admin.ModelAdmin):
    # ...
    list_display = ('Title', 'Year', 'Poster', 'imdbID')
    search_fields = ['Title', 'imdbID']


admin.site.register(Film, FilmAdmin)
