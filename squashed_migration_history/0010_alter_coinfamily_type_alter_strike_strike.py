# Generated by Django 4.2.2 on 2023-07-13 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0009_alter_coinbasemodel_options_alter_coinfamily_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinfamily',
            name='type',
            field=models.CharField(choices=[('Gold', 'Gold'), ('Silver', 'Silver'), ('Clad', 'Clad'), ('Copper', 'Copper')], max_length=20),
        ),
        migrations.AlterField(
            model_name='strike',
            name='strike',
            field=models.CharField(choices=[('MS', 'Business/Mint State'), ('PR', 'Proof'), ('RPR', 'Reverse Proof'), ('PL', 'Proof Like'), ('DMPL', 'DMPL'), ('STN', 'Satin'), ('BRN', 'Burnished')], default='MS', max_length=4, unique=True),
        ),
    ]