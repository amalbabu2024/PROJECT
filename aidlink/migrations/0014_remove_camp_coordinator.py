# Generated by Django 4.2.5 on 2023-11-28 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0013_camp_coordinator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='coordinator',
        ),
    ]
