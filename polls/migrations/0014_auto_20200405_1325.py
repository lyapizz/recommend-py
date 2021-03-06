# Generated by Django 2.2.11 on 2020-04-05 10:25

from decimal import Decimal

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('polls', '0013_auto_20200403_0100'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='average',
            field=models.DecimalField(decimal_places=3, default=Decimal('0'), max_digits=6),
        ),
        migrations.AddField(
            model_name='rating',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE,
                                    to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='rating',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='rating',
            name='object_id',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='total',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together={('content_type', 'object_id')},
        ),
        migrations.DeleteModel(
            name='MyRating',
        ),
    ]
