# Generated by Django 3.1.7 on 2022-11-09 16:41

from django.db import migrations, models
import math_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0004_auto_20221109_1622'),
    ]

    operations = [
        migrations.AddField(
            model_name='ucebnice',
            name='obrazek',
            field=models.ImageField(default=None, upload_to=math_app.models.get_image_ucebnice),
        ),
    ]
