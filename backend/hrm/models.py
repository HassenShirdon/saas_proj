from django.db import models
from django.core.exceptions import ValidationError

class Department(models.Model):
    """Represents a department in the HRM system."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    manager = models.ForeignKey('Employee', on_delete=models.SET_NULL, 
                              null=True, blank=True, related_name='managed_department')
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

class Employee(models.Model):
    """Represents an employee in the HRM system."""
    employee_id = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Removed primary_key=True
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_hired = models.DateField(auto_now_add=True)
    position = models.CharField(max_length=100, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, 
                                 null=True, blank=True, related_name='employees')
    manager = models.ForeignKey('self', on_delete=models.SET_NULL, 
                              null=True, blank=True, related_name='subordinates')
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('terminated', 'Terminated')
    ], default='active')

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

class SalaryHistory(models.Model):
    """Track salary changes over time"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salary_history')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    effective_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.employee} - ${self.amount} (from {self.effective_date})"
    
    class Meta:
        verbose_name = "Salary History"
        verbose_name_plural = "Salary Histories"
        ordering = ['-effective_date']

class PayrollRecord(models.Model):
    """Individual payroll payments"""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='payroll_records')
    pay_period_start = models.DateField()
    pay_period_end = models.DateField()
    gross_amount = models.DecimalField(max_digits=10, decimal_places=2)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    net_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.pay_period_start} to {self.pay_period_end}"

    class Meta:
        verbose_name = "Payroll Record"
        verbose_name_plural = "Payroll Records"
        unique_together = ('employee', 'pay_period_start', 'pay_period_end')

class Attendance(models.Model):
    """Represents an employee's attendance record."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(blank=True, null=True)
    total_hours = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=[
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
        ('half_day', 'Half Day')
    ], default='present')

    def save(self, *args, **kwargs):
        # Calculate total hours if both check_in and check_out are provided
        if self.check_in_time and self.check_out_time:
            time_diff = self.check_out_time - self.check_in_time
            self.total_hours = round(time_diff.total_seconds() / 3600, 2)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee} - {self.date} ({self.status})"

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        unique_together = ('employee', 'date')

class LeaveType(models.Model):
    """Different types of leave available"""
    name = models.CharField(max_length=50, unique=True)
    days_allowed_per_year = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = "Leave Type"
        verbose_name_plural = "Leave Types"

class LeaveRequest(models.Model):
    """Represents a leave request made by an employee."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    leave_type = models.ForeignKey(LeaveType, on_delete=models.CASCADE, related_name='requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')
    approved_by = models.ForeignKey(Employee, on_delete=models.SET_NULL, 
                                  null=True, blank=True, related_name='approved_leaves')
    applied_date = models.DateTimeField(auto_now_add=True)
    processed_date = models.DateTimeField(null=True, blank=True)

    def clean(self):
        if self.start_date and self.end_date and self.start_date > self.end_date:
            raise ValidationError('Start date cannot be after end date')

    @property
    def duration_days(self):
        if self.start_date and self.end_date:
            return (self.end_date - self.start_date).days + 1
        return 0

    def __str__(self):
        return f"{self.employee} - {self.leave_type} ({self.start_date} to {self.end_date}) - {self.status}"

    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"
        ordering = ['-applied_date']

class PerformanceReview(models.Model):
    """Represents a performance review for an employee."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    reviewer = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='reviews_given')
    review_period_start = models.DateField()
    review_period_end = models.DateField()
    review_date = models.DateField()
    rating = models.IntegerField(choices=[
        (1, 'Poor'),
        (2, 'Below Average'),
        (3, 'Average'),
        (4, 'Good'),
        (5, 'Excellent')
    ])
    goals_achieved = models.TextField(blank=True, null=True)
    areas_of_improvement = models.TextField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    next_review_date = models.DateField(null=True, blank=True)

    def clean(self):
        if self.review_period_start and self.review_period_end and self.review_period_start > self.review_period_end:
            raise ValidationError('Review period start date cannot be after end date')

    def __str__(self):
        return f"{self.employee} - {self.review_date} (Rating: {self.rating})"

    class Meta:
        verbose_name = "Performance Review"
        verbose_name_plural = "Performance Reviews"
        unique_together = ('employee', 'review_period_start', 'review_period_end')