from django.contrib import admin

# Register your models here.
from .models import (
    Employee,
    Department,
    Attendance,
    SalaryHistory,
    LeaveType,
    LeaveRequest,
    PerformanceReview,
    PayrollRecord,
)

admin.site.register(Employee)
admin.site.register(Department)
admin.site.register(Attendance)
admin.site.register(SalaryHistory)
admin.site.register(LeaveRequest)
admin.site.register(LeaveType)
admin.site.register(PayrollRecord)
admin.site.register(PerformanceReview)

