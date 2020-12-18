# Generated by Django 3.0.1 on 2020-12-17 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_remove_project_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
