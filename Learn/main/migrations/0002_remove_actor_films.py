# Generated by Django 4.2.3 on 2023-07-16 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='films',
        ),
    ]
