# Generated by Django 3.0.5 on 2020-04-19 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_member_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='age',
        ),
    ]
