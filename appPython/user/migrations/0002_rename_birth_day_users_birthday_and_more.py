# Generated by Django 4.0.3 on 2022-05-05 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='birth_day',
            new_name='birthDay',
        ),
        migrations.RenameField(
            model_name='users',
            old_name='last_name',
            new_name='lastName',
        ),
    ]
