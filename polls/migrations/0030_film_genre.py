# Generated by Django 2.2.11 on 2020-05-17 18:04

from django.db import migrations, models

from polls.actions.films.omdp import getByImdbID
from polls.models import Film


def set_my_defaults(apps, schema_editor):
    for film in Film.objects.all().iterator():
        data = getByImdbID(film.imdbID)
        film.genre = data['Genre']
        film.save()


def reverse_func(apps, schema_editor):
    pass  # code for reverting migration, if any


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0029_auto_20200503_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='genre',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.RunPython(set_my_defaults, reverse_func),
    ]
