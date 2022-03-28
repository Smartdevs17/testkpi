# Generated by Django 3.2.12 on 2022-03-28 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0007_auto_20220321_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank952', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design686', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp328', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype102', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp7723', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kpd',
            name='period',
            field=models.DateField(choices=[(datetime.date(2022, 3, 1), 'P:3:2022'), (datetime.date(2022, 4, 1), 'P:4:2022'), (datetime.date(2022, 5, 1), 'P:5:2022'), (datetime.date(2022, 6, 1), 'P:6:2022'), (datetime.date(2022, 7, 1), 'P:7:2022'), (datetime.date(2022, 8, 1), 'P:8:2022'), (datetime.date(2022, 9, 1), 'P:9:2022'), (datetime.date(2022, 10, 1), 'P:10:2022'), (datetime.date(2022, 11, 1), 'P:11:2022'), (datetime.date(2022, 12, 1), 'P:12:2022')], default='', max_length=70),
        ),
        migrations.AlterField(
            model_name='kpiscorepenalty',
            name='percentage_penalty',
            field=models.IntegerField(default=0.0),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc309', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub243', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit996', max_length=70, primary_key=True, serialize=False),
        ),
    ]