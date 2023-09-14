# Generated by Django 4.2.2 on 2023-09-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0042_alter_coinfamily_type'),
        ('customers', '0002_alter_customers_options_customers_is_deleted'),
        ('invoice', '0002_remove_salesinvoice_invoice_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesinvoice',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='customers.customers'),
        ),
        migrations.RemoveField(
            model_name='salesinvoice',
            name='sales_item',
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='sales_item',
            field=models.ManyToManyField(related_name='sales', to='coins.coinbasemodel'),
        ),
    ]
