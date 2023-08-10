# Generated by Django 4.2.2 on 2023-07-12 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coins', '0007_selectonemint_alter_coinbasemodel_mint_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectMints',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('philadelphia', models.BooleanField(default=False)),
                ('san_francisco', models.BooleanField(default=False)),
                ('denver', models.BooleanField(default=False)),
                ('carson_city', models.BooleanField(default=False)),
                ('west_point', models.BooleanField(default=False)),
                ('charlotte', models.BooleanField(default=False)),
                ('new_orleans', models.BooleanField(default=False)),
                ('dahlonega', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Select Multiple Mints',
                'verbose_name_plural': 'Select Multiple Mints',
            },
        ),
        migrations.CreateModel(
            name='Strike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('strike', models.CharField(choices=[('MS', 'Business/Mint State'), ('PR', 'Proof'), ('RPR', 'Reverse Proof'), ('PL', 'Proof Like'), ('DMPL', 'DMPL'), ('STN', 'Satin'), ('BRN', 'Burnished')], default='MS', max_length=4)),
            ],
            options={
                'verbose_name': 'Strike',
                'verbose_name_plural': 'Strikes',
            },
        ),
        migrations.AlterModelOptions(
            name='selectonemint',
            options={'verbose_name': 'Select One Mint', 'verbose_name_plural': 'Select One Mint'},
        ),
        migrations.RenameField(
            model_name='selectonemint',
            old_name='mint_name',
            new_name='coin_mint',
        ),
        migrations.RemoveField(
            model_name='coinbasemodel',
            name='grade2',
        ),
        migrations.AlterField(
            model_name='coinbasemodel',
            name='strike',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='coins.strike'),
        ),
    ]