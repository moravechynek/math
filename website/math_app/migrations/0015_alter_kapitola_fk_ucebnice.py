# Generated by Django 4.1.3 on 2022-11-24 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('math_app', '0014_alter_kapitola_fk_ucebnice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kapitola',
            name='FK_ucebnice',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='math_app.ucebnice'),
        ),
    ]