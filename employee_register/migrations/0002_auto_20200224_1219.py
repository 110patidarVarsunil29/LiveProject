# Generated by Django 3.0.2 on 2020-02-24 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Department'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='employee',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee_register.Manager'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='password',
            field=models.CharField(default='Welcome@1234', editable=False, max_length=50),
        ),
    ]
