# Generated by Django 4.2.5 on 2023-11-09 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0010_remove_camp_location_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='camp_location',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
