# Generated by Django 4.0.5 on 2022-06-13 04:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0003_rename_profile_picture_profile_profile_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile_photo',
            new_name='profile_picture',
        ),
    ]