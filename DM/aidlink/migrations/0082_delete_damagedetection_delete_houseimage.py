# Generated by Django 4.2.5 on 2024-04-06 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0081_houseimage_damagedetection'),
    ]

    operations = [
        migrations.DeleteModel(
            name='DamageDetection',
        ),
        migrations.DeleteModel(
            name='HouseImage',
        ),
    ]
