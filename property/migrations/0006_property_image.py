# Generated by Django 3.0.4 on 2020-04-19 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_auto_20200419_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='image',
            field=models.ImageField(null=True, upload_to='property/'),
        ),
    ]
