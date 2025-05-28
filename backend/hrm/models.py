from django.db import models

# Create your models here.
class Employee(models.Model):
    """Represents an employee in the HRM system."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    date_hired = models.DateField(auto_now_add=True)
    position = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

class Department(models.Model):
    """Represents a department in the HRM system."""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"

class Attendance(models.Model):
    """Represents an employee's attendance record."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='attendances')
    date = models.DateField()
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.date}"

    class Meta:
        verbose_name = "Attendance"
        verbose_name_plural = "Attendances"
        unique_together = ('employee', 'date')

class Salary(models.Model): 
    """Represents an employee's salary record."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='salaries')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.employee} - {self.amount} on {self.payment_date}"

    class Meta:
        verbose_name = "Salary"
        verbose_name_plural = "Salaries"
        unique_together = ('employee', 'payment_date')

class LeaveRequest(models.Model):
    """Represents a leave request made by an employee."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='leave_requests')
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], default='pending')

    def __str__(self):
        return f"{self.employee} - {self.start_date} to {self.end_date} ({self.status})"

    class Meta:
        verbose_name = "Leave Request"
        verbose_name_plural = "Leave Requests"
        unique_together = ('employee', 'start_date', 'end_date')

class PerformanceReview(models.Model):
    """Represents a performance review for an employee."""
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name='performance_reviews')
    review_date = models.DateField()
    reviewer = models.CharField(max_length=100)
    comments = models.TextField(blank=True, null=True)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.employee} - {self.review_date} ({self.rating})"

    class Meta:
        verbose_name = "Performance Review"
        verbose_name_plural = "Performance Reviews"
        unique_together = ('employee', 'review_date')