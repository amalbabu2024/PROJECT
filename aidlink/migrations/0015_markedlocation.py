# Generated by Django 4.2.5 on 2023-11-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0014_remove_camp_coordinator'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkedLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]
