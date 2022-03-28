# Generated by Django 3.2.12 on 2022-03-28 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0009_auto_20220328_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank615', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design712', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp319', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype800', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp8540', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc691', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub132', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit901', max_length=70, primary_key=True, serialize=False),
        ),
    ]