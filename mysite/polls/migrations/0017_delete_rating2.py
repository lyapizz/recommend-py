# Generated by Django 2.2.11 on 2020-04-05 11:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0016_rating2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rating2',
        ),
    ]