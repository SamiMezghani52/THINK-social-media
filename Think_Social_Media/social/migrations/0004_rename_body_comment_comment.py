# Generated by Django 3.2.6 on 2021-08-28 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='body',
            new_name='comment',
        ),
    ]
