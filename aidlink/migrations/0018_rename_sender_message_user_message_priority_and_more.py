# Generated by Django 4.2.5 on 2023-11-30 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aidlink', '0017_messagecategory_message'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='sender',
            new_name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='priority',
            field=models.CharField(choices=[('Urgent', 'Urgent/High Priority'), ('Important', 'Important/Action Required'), ('Informational', 'Informational/Update'), ('Decision', 'Decision/Approval Needed'), ('Routine', 'Routine/General Communication'), ('FYI', 'FYI/Information Only'), ('Acknowledgment', 'Acknowledgment/Confirmation'), ('Appreciation', 'Appreciation/Recognition'), ('Miscellaneous', 'Miscellaneous/Other')], default='Informational', max_length=20),
        ),
        migrations.AlterField(
            model_name='message',
            name='category',
            field=models.CharField(max_length=50),
        ),
        migrations.DeleteModel(
            name='MessageCategory',
        ),
    ]
