# Generated by Django 3.0.2 on 2020-02-23 10:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departmentname', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mangername', models.CharField(max_length=50)),
                ('departmentid', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='employee_register.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('password', models.CharField(default=True,max_length=50)),
                ('empcode', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('email', models.CharField(default='', max_length=30)),
                ('date_of_joining', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('department', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee_register.Department')),
                ('manager', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='employee_register.Manager')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Position')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='managerid',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to='employee_register.Manager'),
        ),
    ]
