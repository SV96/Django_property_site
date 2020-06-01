# Generated by Django 3.0.4 on 2020-04-19 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_property_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image',
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(choices=[('R', 'rent'), ('S', 'sale')], max_length=10),
        ),
    ]