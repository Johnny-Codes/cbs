# Generated by Django 4.2.2 on 2023-07-18 02:10

from django.db import migrations, models
import images.models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(unique=True, upload_to=images.models.image_file_path),
        ),
    ]
