# Generated by Django 5.1.9 on 2025-05-28 10:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_hired', models.DateField(auto_now_add=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in_time', models.DateTimeField()),
                ('check_out_time', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
                'unique_together': {('employee', 'date')},
            },
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Leave Request',
                'verbose_name_plural': 'Leave Requests',
                'unique_together': {('employee', 'start_date', 'end_date')},
            },
        ),
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_date', models.DateField()),
                ('reviewer', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True, null=True)),
                ('rating', models.IntegerField(default=0)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_reviews', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Performance Review',
                'verbose_name_plural': 'Performance Reviews',
                'unique_together': {('employee', 'review_date')},
            },
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salaries', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Salary',
                'verbose_name_plural': 'Salaries',
                'unique_together': {('employee', 'payment_date')},
            },
        ),
    ]
