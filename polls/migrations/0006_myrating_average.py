# Generated by Django 2.2.11 on 2020-03-24 20:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0005_auto_20200324_2348'),
    ]

    operations = [
        migrations.AddField(
            model_name='myrating',
            name='average',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
