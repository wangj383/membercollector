# Generated by Django 3.0.5 on 2020-04-21 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0009_auto_20200420_2134'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('place', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='member',
            name='event',
            field=models.ManyToManyField(to='main_app.Event'),
        ),
    ]