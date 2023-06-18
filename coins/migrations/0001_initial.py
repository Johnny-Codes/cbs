# Generated by Django 4.2.2 on 2023-06-18 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
        ('accounts', '0002_business_user_business'),
    ]

    operations = [
        migrations.CreateModel(
            name='SilverDollars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dollar_type', models.CharField(choices=[('Flowing Hair Dollar', 'Flowing Hair Dollar'), ('Draped Bust Dollar', 'Draped Bust Dollar'), ('Liberty Seated Dollar', 'Liberty Seated Dollar'), ('Trade Dollar', 'Trade Dollar'), ('Morgan Dollar', 'Morgan Dollar'), ('Peace Dollar', 'Peace Dollar'), ('Ike Dollar', 'Ike Dollar'), ('Susan B. Anthony Dollar', 'Susan B. Anthony Dollar'), ('Sacagawea Dollar', 'Sacagawea Dollar'), ('Presidential Dollar', 'Presidential Dollar'), ('American Innovation Dollar', 'American Innovation Dollar')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='CoinInventory',
            fields=[
                ('createdupdated_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.createdupdated')),
                ('year', models.IntegerField()),
                ('mint', models.CharField(choices=[('P', 'P'), ('S', 'S'), ('D', 'D'), ('CC', 'CC'), ('W', 'W'), ('C', 'C'), ('O', 'O'), ('M', 'M')], default='P', max_length=2)),
                ('denomination', models.CharField(choices=[('$50', '$50'), ('$25', '$25'), ('$20', '$20'), ('$10', '$10'), ('$5', '$5'), ('$4', '$4'), ('$3', '$3'), ('$2.5', '$2.5'), ('$1', '$1'), ('50C', '50C'), ('25C', '25C'), ('20C', '20C'), ('10C', '10C'), ('5C', '5C'), ('3CN', '3CN'), ('3CS', '3CS'), ('2C', '2C'), ('1C', '1C'), ('H1C', 'H1C')], default='$1', max_length=4)),
                ('description', models.TextField(blank=True, null=True)),
                ('strike', models.CharField(choices=[('MS', 'Business/Mint State'), ('PR', 'Proof'), ('RPR', 'Reverse Proof'), ('PL', 'Proof Like'), ('DMPL', 'DMPL'), ('STN', 'Satin'), ('BRN', 'Burnished')], default='MS', max_length=4)),
                ('grading', models.CharField(choices=[('PCGS', 'PCGS'), ('NGC', 'NGC'), ('PCGSCAC', 'PCGS CAC'), ('NGCCAC', 'NGC CAC'), ('ANACS', 'ANACS'), ('ICG', 'ICG'), ('PCGSoNGC', 'PCGS or NGC'), ('PCGSoNGCaCAC', 'PCGS or NGC and CAC'), ('Ungraded', 'Ungraded')], default='PCGS', max_length=15)),
                ('grade', models.CharField(choices=[('70', '70'), ('69+', '69+'), ('69', '69'), ('68+', '68+'), ('68', '68'), ('67+', '67+'), ('67', '67'), ('66+', '66+'), ('66', '66'), ('65+', '65+'), ('65', '65'), ('64+', '64+'), ('64', '64'), ('63+', '63+'), ('63', '63'), ('62+', '62+'), ('62', '62'), ('61+', '61+'), ('61', '61'), ('60+', '60+'), ('60', '60'), ('58', '58'), ('55', '55'), ('50', '50'), ('45', '45'), ('40', '40'), ('35', '35'), ('30', '30'), ('25', '25'), ('20', '20'), ('15', '15'), ('12', '12'), ('10', '10'), ('08', '08'), ('06', '06'), ('04', '04'), ('03', '03'), ('02', '02'), ('01', '01'), ('BU', 'BU'), ('CU', 'CU'), ('UNC', 'UNC'), ('AU+', 'AU+'), ('AU', 'AU'), ('XF+', 'XF+'), ('XF', 'XF'), ('VF+', 'VF+'), ('VF', 'VF'), ('F+', 'F+'), ('F', 'F'), ('VG+', 'VG+'), ('VG', 'VG'), ('G+', 'G+'), ('G', 'G')], default='70', max_length=3)),
                ('business', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='accounts.business')),
            ],
            options={
                'abstract': False,
            },
            bases=('core.createdupdated', models.Model),
        ),
    ]
