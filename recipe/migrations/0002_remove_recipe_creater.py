# Generated by Django 2.2 on 2020-01-30 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='creater',
        ),
    ]
