# Generated by Django 3.0.2 on 2020-02-25 06:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0003_auto_20200224_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='empcode',
        ),
    ]
