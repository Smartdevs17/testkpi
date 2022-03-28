# Generated by Django 3.2.12 on 2022-03-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0010_auto_20220328_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank947', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design522', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp500', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype175', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp8247', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc663', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub526', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit519', max_length=70, primary_key=True, serialize=False),
        ),
    ]
