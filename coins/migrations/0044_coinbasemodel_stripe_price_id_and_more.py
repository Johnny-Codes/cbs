# Generated by Django 5.0.2 on 2024-06-25 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0043_coinbasemodel_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinbasemodel',
            name='stripe_price_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='coinbasemodel',
            name='stripe_product_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
