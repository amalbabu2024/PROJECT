# Generated by Django 4.2.5 on 2023-12-04 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0026_rename_qualifications_volunteerrequest_additional_information_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerrequest',
            old_name='additional_information',
            new_name='educational_qualifications',
        ),
        migrations.RenameField(
            model_name='volunteerrequest',
            old_name='languages_spoken',
            new_name='health_condition',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='agreement_and_code_of_conduct',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_days_flexible',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_days_weekdays',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_days_weekends',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_for_deployment',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_times_afternoons',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_times_evenings',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='availability_times_mornings',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='background_check_consent',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='certifications_cpr',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='certifications_other',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='city',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='media_release_consent',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='other_considerations',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='phone_home',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='physical_limitations',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='references',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='relevant_skills_language_proficiency',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='relevant_skills_logistics',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='relevant_skills_other',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='signature',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='state',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='training_availability',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='training_method_in_person',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='training_method_online',
        ),
        migrations.RemoveField(
            model_name='volunteerrequest',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='volunteerrequest',
            name='blood_group',
            field=models.CharField(default='', max_length=5),
        ),
    ]
