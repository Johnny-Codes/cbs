# Generated by Django 4.2.2 on 2023-07-14 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0010_alter_coinfamily_type_alter_strike_strike'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinfamily',
            name='type',
            field=models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Clad', 'Clad'), ('Copper', 'Copper')], max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='cointypename',
            name='coin_type',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='selectonemint',
            name='coin_mint',
            field=models.CharField(choices=[('P', 'Philadelphia Mint'), ('S', 'San Francisco Mint'), ('D', 'Denver Mint'), ('CC', 'Carson City Mint'), ('W', 'West Point Mint'), ('C', 'Charlotte Mint'), ('O', 'New Orleans Mint'), ('DL', 'Dahlonega Mint')], default='P', max_length=2, unique=True),
        ),
    ]
