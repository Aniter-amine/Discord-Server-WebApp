# Generated by Django 3.0.1 on 2020-12-17 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_project_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='author',
        ),
    ]
