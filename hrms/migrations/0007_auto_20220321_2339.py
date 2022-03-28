# Generated by Django 3.2.12 on 2022-03-21 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0006_auto_20220321_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='bank_id',
            field=models.CharField(default='bank852', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='designation',
            name='design_id',
            field=models.CharField(default='design543', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp442', max_length=70),
        ),
        migrations.AlterField(
            model_name='employeetype',
            name='employeetype_id',
            field=models.CharField(default='emptype476', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employment',
            name='employ_id',
            field=models.CharField(default='emp2318', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kpi_evalutation',
            name='comment',
            field=models.CharField(choices=[('excellent', 'EXCELLENT'), ('very good', 'VERY GOOD'), ('good', 'GOOD'), ('satisfactory', 'SATISFACTORY'), ('unsatisfactory', 'UNSATISFACTORY')], default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='position',
            name='position_code',
            field=models.CharField(default='pc378', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='sbu_directorate',
            name='sbu_id',
            field=models.CharField(default='sub363', max_length=70, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='unit',
            name='unit_id',
            field=models.CharField(default='unit611', max_length=70, primary_key=True, serialize=False),
        ),
    ]
