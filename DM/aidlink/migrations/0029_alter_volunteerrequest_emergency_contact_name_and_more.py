# Generated by Django 4.2.5 on 2023-12-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0028_remove_volunteerrequest_areas_of_interest_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerrequest',
            name='emergency_contact_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='volunteerrequest',
            name='emergency_contact_phone',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='volunteerrequest',
            name='full_name',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='volunteerrequest',
            name='gender',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='volunteerrequest',
            name='phone_mobile',
            field=models.TextField(default=''),
        ),
    ]
