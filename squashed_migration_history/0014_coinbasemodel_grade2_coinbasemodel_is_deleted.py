# Generated by Django 4.2.2 on 2023-07-14 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0013_alter_coingrades_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coinbasemodel',
            name='grade2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coin_grade_2', to='coins.coingrades'),
        ),
        migrations.AddField(
            model_name='coinbasemodel',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]