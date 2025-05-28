from django.contrib import admin

# Register your models here.
from .models import (
    Employee,
    Department,
    Attendance,
    Salary,
    LeaveRequest,
    PerformanceReview,
)

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(Salary)
admin.site.register(LeaveRequest)
admin.site.register(PerformanceReview)

