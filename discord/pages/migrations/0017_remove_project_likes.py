# Generated by Django 3.0.1 on 2020-12-18 00:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0016_project_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
    ]