# Generated by Django 4.2.2 on 2023-07-17 01:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0014_coinbasemodel_grade2_coinbasemodel_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cointypename',
            name='denominations',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coin_type_name', to='coins.denominations'),
        ),
        migrations.AlterField(
            model_name='denominations',
            name='denomination_of_coin',
            field=models.CharField(choices=[('$50', '$50'), ('$25', '$25'), ('$20', '$20'), ('$10', '$10'), ('$5', '$5'), ('$4', '$4'), ('$3', '$3'), ('$2.5', '$2.5'), ('$1', '$1'), ('50C', '50C'), ('25C', '25C'), ('20C', '20C'), ('10C', '10C'), ('5C', '5C'), ('3CN', '3CN'), ('3CS', '3CS'), ('2C', '2C'), ('1C', '1C'), ('H1C', 'H1C')], default='$1', max_length=4, unique=True),
        ),
        migrations.AlterField(
            model_name='denominations',
            name='family',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='denominations', to='coins.coinfamily'),
        ),
    ]
