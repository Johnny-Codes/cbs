# Generated by Django 5.0.2 on 2024-02-29 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sku',
            name='is_deleted',
        ),
    ]
