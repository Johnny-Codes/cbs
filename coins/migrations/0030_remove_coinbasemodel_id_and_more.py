# Generated by Django 4.2.2 on 2023-07-19 02:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('coins', '0029_alter_coinbasemodel_images_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coinbasemodel',
            name='id',
        ),
        migrations.RemoveField(
            model_name='coinbasemodel',
            name='is_deleted',
        ),
        migrations.AddField(
            model_name='coinbasemodel',
            name='sku_ptr',
            field=models.OneToOneField(auto_created=True, default=1, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.sku'),
            preserve_default=False,
        ),
    ]