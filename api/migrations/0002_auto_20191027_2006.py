# Generated by Django 2.2.6 on 2019-10-27 20:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profiles',
            old_name='create_profile_for',
            new_name='creating_profile_for',
        ),
    ]