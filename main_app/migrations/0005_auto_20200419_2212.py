# Generated by Django 3.0.5 on 2020-04-20 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='members',
            new_name='member',
        ),
    ]
