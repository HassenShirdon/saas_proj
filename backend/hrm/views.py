from rest_framework import generics
from .models import (
    Employee,
    Department,
    PerformanceReview,
    Attendance,
    LeaveRequest,
    Salary,
)

from .serializers import (
    EmployeeSerializer,
    DepartmentSerializer,
    attendanceSerializer,
    LeaveRequestSerializer,
    PerformanceReviewSerializer,
    SalarySerializer,
)
# Create your views here.

class EmployeeList(generics.ListCreateAPIView):
    """API view to list and create employees."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'date_hired', 'position']
    ordering_fields = ['first_name', 'last_name', 'date_hired']

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an employee."""
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    filterset_fields = ['first_name', 'last_name', 'email', 'phone_number', 'date_of_birth', 'date_hired', 'position']
    lookup_field = 'email'  

class DepartmentList(generics.ListCreateAPIView):
    """API view to list and create departments."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['name', 'description']
    ordering_fields = ['name']

class DepartmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a department."""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    filterset_fields = ['name', 'description']
    lookup_field = 'name'

class AttendanceList(generics.ListCreateAPIView):
    """API view to list and create attendance records."""
    queryset = Attendance.objects.all()
    serializer_class = attendanceSerializer
    filterset_fields = ['employee', 'date', 'check_in_time', 'check_out_time']
    ordering_fields = ['date', 'check_in_time'] 

class AttendanceDetail(generics.RetrieveUpdateDestroyAPIView): 
    """API view to retrieve, update or delete an attendance record."""
    queryset = Attendance.objects.all()
    serializer_class = attendanceSerializer
    filterset_fields = ['employee', 'date', 'check_in_time', 'check_out_time']
    lookup_field = 'date'  # Assuming date is unique per employee
    ordering_fields = ['date', 'check_in_time']

class LeaveRequestList(generics.ListCreateAPIView):
    """API view to list and create leave requests."""
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filterset_fields = ['employee', 'start_date', 'end_date', 'status']
    ordering_fields = ['start_date', 'end_date', 'status']  

class LeaveRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a leave request."""
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    filterset_fields = ['employee', 'start_date', 'end_date', 'status']
    lookup_field = 'id'  # Assuming ID is used for lookups
    ordering_fields = ['start_date', 'end_date', 'status']

class PerformanceReviewList(generics.ListCreateAPIView):
    """API view to list and create performance reviews."""
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    filterset_fields = ['employee', 'review_date', 'rating']
    ordering_fields = ['review_date', 'rating']

class performanceReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a performance review."""
    queryset = PerformanceReview.objects.all()
    serializer_class = PerformanceReviewSerializer
    filterset_fields = ['employee', 'review_date', 'rating']
    lookup_field = 'id'  # Assuming ID is used for lookups
    ordering_fields = ['review_date', 'rating']

class SalaryList(generics.ListCreateAPIView):
    """API view to list and create salary records."""
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    filterset_fields = ['employee', 'payment_date', 'amount']
    ordering_fields = ['payment_date', 'amount']

class SalaryDetail(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a salary record."""
    queryset = Salary.objects.all()
    serializer_class = SalarySerializer
    filterset_fields = ['employee', 'payment_date', 'amount']
    lookup_field = 'id'  # Assuming ID is used for lookups
    ordering_fields = ['payment_date', 'amount']

