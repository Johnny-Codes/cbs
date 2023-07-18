# Generated by Django 4.2.2 on 2023-07-18 02:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0018_coinbasemodel_is_bulk'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinbasemodel',
            name='mints',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mints', to='coins.selectmints'),
        ),
        migrations.AlterField(
            model_name='coinbasemodel',
            name='mint',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mint', to='coins.selectonemint'),
        ),
    ]
