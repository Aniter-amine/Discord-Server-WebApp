# Generated by Django 3.0.1 on 2020-12-17 18:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0011_auto_20201217_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='author_avatar',
            field=models.CharField(default=django.utils.timezone.now, max_length=256),
            preserve_default=False,
        ),
    ]
