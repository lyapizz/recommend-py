# Generated by Django 2.2.11 on 2020-05-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0026_film_imdburl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='imdbUrl',
            field=models.CharField(max_length=1000, verbose_name='IMDB url'),
        ),
    ]
