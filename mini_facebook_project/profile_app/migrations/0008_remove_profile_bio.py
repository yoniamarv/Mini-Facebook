# Generated by Django 2.1.5 on 2019-01-20 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_auto_20190117_1507'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
    ]
