# Generated by Django 3.2.6 on 2021-08-27 21:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_on',
        ),
    ]