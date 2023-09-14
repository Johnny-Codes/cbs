# Generated by Django 4.2.2 on 2023-09-13 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customers_options_customers_is_deleted'),
        ('invoice', '0003_alter_salesinvoice_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesinvoice',
            name='customer',
        ),
        migrations.AddField(
            model_name='salesinvoice',
            name='customer',
            field=models.ManyToManyField(related_name='sales', to='customers.customers'),
        ),
    ]