# Generated by Django 3.2.12 on 2022-06-03 13:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='unit',
            name='head_of_unit',
        ),
    ]