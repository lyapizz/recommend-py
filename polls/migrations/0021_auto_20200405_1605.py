# Generated by Django 2.2.11 on 2020-04-05 13:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0020_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myrating',
            name='film',
        ),
        migrations.RemoveField(
            model_name='myrating',
            name='score',
        ),
        migrations.RemoveField(
            model_name='myrating',
            name='user',
        ),
    ]
