# Generated by Django 4.1.3 on 2022-11-24 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0016_reseni_cas'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseni',
            name='uzivatel',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]