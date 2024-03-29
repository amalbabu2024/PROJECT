# Generated by Django 4.2.5 on 2024-02-08 06:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0035_manager_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamleader',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_leader', to='aidlink.organization'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_member', to='aidlink.organization'),
        ),
    ]
