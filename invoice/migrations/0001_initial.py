# Generated by Django 4.2.2 on 2023-09-06 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0002_alter_customers_options_customers_is_deleted'),
        ('coins', '0042_alter_coinfamily_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(editable=False, max_length=10, unique=True)),
                ('invoice_date', models.DateTimeField(auto_now_add=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='customers.customers')),
                ('sales_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales', to='coins.coinbasemodel')),
            ],
        ),
    ]
