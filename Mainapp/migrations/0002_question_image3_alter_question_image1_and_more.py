# Generated by Django 5.0.1 on 2024-01-18 18:33

import Mainapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to=Mainapp.models.upload_to),
        ),
        migrations.AlterField(
            model_name='question',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=Mainapp.models.upload_to),
        ),
        migrations.AlterField(
            model_name='question',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to=Mainapp.models.upload_to),
        ),
    ]
