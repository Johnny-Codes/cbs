# Generated by Django 4.2.2 on 2023-07-18 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0025_alter_gradingservices_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinbasemodel',
            name='grading',
        ),
        migrations.AddField(
            model_name='coinbasemodel',
            name='grading',
            field=models.ManyToManyField(related_name='grading_service', to='coins.gradingservices'),
        ),
    ]