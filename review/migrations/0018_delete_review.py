# Generated by Django 4.0.5 on 2022-06-14 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0017_remove_review_project'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Review',
        ),
    ]
