# Generated by Django 2.2.11 on 2020-03-28 17:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('polls', '0009_auto_20200328_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='Year',
            field=models.CharField(default='0', max_length=200),
        ),
    ]