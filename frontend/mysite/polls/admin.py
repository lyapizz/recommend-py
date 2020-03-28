from django.contrib import admin

from .models import Film, Choice


class ChoiceInline(admin.TabularInline):
    # ...
    model = Choice
    extra = 3


class FilmAdmin(admin.ModelAdmin):
    # ...
    list_display = ('Title', 'Year', 'Poster', 'imdbID')
    search_fields = ['Title', 'imdbID']
    inlines = [ChoiceInline]


admin.site.register(Film, FilmAdmin)
