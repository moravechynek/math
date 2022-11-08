# Generated by Django 4.1.3 on 2022-11-08 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0002_auto_20221107_1913'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reseni',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reseni', models.CharField(max_length=200)),
                ('FK_priklad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='math_app.priklad')),
            ],
            options={
                'verbose_name': 'Řešení',
                'verbose_name_plural': 'Řešení',
            },
        ),
    ]
