# Generated by Django 4.2.2 on 2023-07-18 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0021_alter_coinbasemodel_mint'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbasemodel',
            name='mint',
            field=models.ManyToManyField(blank=True, related_name='mint', to='coins.selectonemint'),
        ),
    ]
