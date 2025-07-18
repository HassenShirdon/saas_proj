# Generated by Django 5.1.10 on 2025-07-15 19:49

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
            name='LeaveType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('days_allowed_per_year', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Leave Type',
                'verbose_name_plural': 'Leave Types',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_id', models.CharField(max_length=20, unique=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('date_hired', models.DateField(auto_now_add=True)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('current_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive'), ('terminated', 'Terminated')], default='active', max_length=20)),
                ('Employee_ID', models.ImageField(blank=True, null=True, upload_to='employees_id/')),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='employees', to='hrm.department')),
                ('manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinates', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Employee',
                'verbose_name_plural': 'Employees',
            },
        ),
        migrations.AddField(
            model_name='department',
            name='manager',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='managed_department', to='hrm.employee'),
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')], default='pending', max_length=20)),
                ('applied_date', models.DateTimeField(auto_now_add=True)),
                ('processed_date', models.DateTimeField(blank=True, null=True)),
                ('approved_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='approved_leaves', to='hrm.employee')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to='hrm.employee')),
                ('leave_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='hrm.leavetype')),
            ],
            options={
                'verbose_name': 'Leave Request',
                'verbose_name_plural': 'Leave Requests',
                'ordering': ['-applied_date'],
            },
        ),
        migrations.CreateModel(
            name='SalaryHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('effective_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('reason', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salary_history', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Salary History',
                'verbose_name_plural': 'Salary Histories',
                'ordering': ['-effective_date'],
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('check_in_time', models.DateTimeField()),
                ('check_out_time', models.DateTimeField(blank=True, null=True)),
                ('total_hours', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late'), ('half_day', 'Half Day')], default='present', max_length=20)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Attendance',
                'verbose_name_plural': 'Attendances',
                'unique_together': {('employee', 'date')},
            },
        ),
        migrations.CreateModel(
            name='PayrollRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pay_period_start', models.DateField()),
                ('pay_period_end', models.DateField()),
                ('gross_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deductions', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('net_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField()),
                ('notes', models.TextField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payroll_records', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Payroll Record',
                'verbose_name_plural': 'Payroll Records',
                'unique_together': {('employee', 'pay_period_start', 'pay_period_end')},
            },
        ),
        migrations.CreateModel(
            name='PerformanceReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_period_start', models.DateField()),
                ('review_period_end', models.DateField()),
                ('review_date', models.DateField()),
                ('rating', models.IntegerField(choices=[(1, 'Poor'), (2, 'Below Average'), (3, 'Average'), (4, 'Good'), (5, 'Excellent')])),
                ('goals_achieved', models.TextField(blank=True, null=True)),
                ('areas_of_improvement', models.TextField(blank=True, null=True)),
                ('comments', models.TextField(blank=True, null=True)),
                ('next_review_date', models.DateField(blank=True, null=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='performance_reviews', to='hrm.employee')),
                ('reviewer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews_given', to='hrm.employee')),
            ],
            options={
                'verbose_name': 'Performance Review',
                'verbose_name_plural': 'Performance Reviews',
                'unique_together': {('employee', 'review_period_start', 'review_period_end')},
            },
        ),
    ]
