# Generated by Django 4.2.2 on 2023-07-18 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0002_alter_images_image'),
        ('coins', '0027_alter_gradingservices_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinbasemodel',
            name='images',
        ),
        migrations.AddField(
            model_name='coinbasemodel',
            name='images',
            field=models.ManyToManyField(blank=True, null=True, to='images.images'),
        ),
    ]
