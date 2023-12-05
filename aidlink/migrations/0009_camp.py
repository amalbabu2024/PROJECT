# Generated by Django 4.2.5 on 2023-11-09 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0008_remove_resource_location_remove_resource_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Camp',
            fields=[
                ('camp_id', models.AutoField(primary_key=True, serialize=False)),
                ('camp_name', models.CharField(max_length=100)),
                ('location_id', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('contact_phone', models.CharField(max_length=15)),
                ('contact_email', models.EmailField(max_length=254)),
            ],
        ),
    ]
