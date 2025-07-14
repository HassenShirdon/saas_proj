from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch
from rest_framework.renderers import JSONRenderer

from .models import (
    Employee,
    Department,
    PerformanceReview,
    Attendance,
    LeaveRequest,
    LeaveType,
    SalaryHistory,
    PayrollRecord,
)

from .serializers import (
    EmployeeSerializer,
    EmployeeDetailSerializer,
    DepartmentSerializer,
    DepartmentDetailSerializer,
    AttendanceSerializer,
    LeaveRequestSerializer,
    LeaveTypeSerializer,
    PerformanceReviewSerializer,
    SalaryHistorySerializer,
    PayrollRecordSerializer,
)

# Employee Views
class EmployeeListCreateView(generics.ListCreateAPIView):
    """API view to list and create employees."""
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = {
        'department': ['exact'],
        'manager': ['exact'],
        'status': ['exact'],
        'position': ['icontains'],
        'date_hired': ['gte', 'lte', 'exact'],
    }
    search_fields = ['first_name', 'last_name', 'email', 'employee_id']
    ordering_fields = ['first_name', 'last_name', 'date_hired', 'employee_id']
    ordering = ['last_name', 'first_name']
    renderer_classes = [JSONRenderer]

    def get_queryset(self):
        return Employee.objects.select_related('department', 'manager').filter(status='active')

class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an employee."""
    serializer_class = EmployeeDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'  # Use primary key for safety

    def get_queryset(self):
        return Employee.objects.select_related(
            'department', 'manager'
        ).prefetch_related(
            'subordinates',
            'attendances',
            'leave_requests',
            'performance_reviews',
            'salary_history'
        )

# Department Views
class DepartmentListCreateView(generics.ListCreateAPIView):
    """API view to list and create departments."""
    queryset = Department.objects.select_related('manager')
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']
    ordering_fields = ['name']
    ordering = ['name']

class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a department."""
    serializer_class = DepartmentDetailSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Department.objects.select_related('manager').prefetch_related(
            Prefetch('employees', queryset=Employee.objects.filter(status='active'))
        )

# Attendance Views
class AttendanceListCreateView(generics.ListCreateAPIView):
    """API view to list and create attendance records."""
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'date': ['gte', 'lte', 'exact'],
        'status': ['exact'],
    }
    ordering_fields = ['date', 'check_in_time']
    ordering = ['-date']

    def get_queryset(self):
        return Attendance.objects.select_related('employee')

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete an attendance record."""
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return Attendance.objects.select_related('employee')

# Leave Type Views
class LeaveTypeListCreateView(generics.ListCreateAPIView):
    """API view to list and create leave types."""
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['name']
    ordering = ['name']

class LeaveTypeDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a leave type."""
    queryset = LeaveType.objects.all()
    serializer_class = LeaveTypeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

# Leave Request Views
class LeaveRequestListCreateView(generics.ListCreateAPIView):
    """API view to list and create leave requests."""
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'leave_type': ['exact'],
        'status': ['exact'],
        'start_date': ['gte', 'lte', 'exact'],
        'end_date': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['start_date', 'end_date', 'applied_date']
    ordering = ['-applied_date']

    def get_queryset(self):
        return LeaveRequest.objects.select_related('employee', 'leave_type', 'approved_by')

class LeaveRequestDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a leave request."""
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return LeaveRequest.objects.select_related('employee', 'leave_type', 'approved_by')

# Performance Review Views
class PerformanceReviewListCreateView(generics.ListCreateAPIView):
    """API view to list and create performance reviews."""
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'reviewer': ['exact'],
        'rating': ['exact', 'gte', 'lte'],
        'review_date': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['review_date', 'rating']
    ordering = ['-review_date']

    def get_queryset(self):
        return PerformanceReview.objects.select_related('employee', 'reviewer')

class PerformanceReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a performance review."""
    serializer_class = PerformanceReviewSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return PerformanceReview.objects.select_related('employee', 'reviewer')

# Salary History Views
class SalaryHistoryListCreateView(generics.ListCreateAPIView):
    """API view to list and create salary history records."""
    serializer_class = SalaryHistorySerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'effective_date': ['gte', 'lte', 'exact'],
        'amount': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['effective_date', 'amount']
    ordering = ['-effective_date']

    def get_queryset(self):
        return SalaryHistory.objects.select_related('employee')

class SalaryHistoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a salary history record."""
    serializer_class = SalaryHistorySerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return SalaryHistory.objects.select_related('employee')

# Payroll Record Views
class PayrollRecordListCreateView(generics.ListCreateAPIView):
    """API view to list and create payroll records."""
    serializer_class = PayrollRecordSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'employee': ['exact'],
        'payment_date': ['gte', 'lte', 'exact'],
        'pay_period_start': ['gte', 'lte', 'exact'],
        'pay_period_end': ['gte', 'lte', 'exact'],
    }
    ordering_fields = ['payment_date', 'pay_period_start']
    ordering = ['-payment_date']

    def get_queryset(self):
        return PayrollRecord.objects.select_related('employee')

class PayrollRecordDetailView(generics.RetrieveUpdateDestroyAPIView):
    """API view to retrieve, update or delete a payroll record."""
    serializer_class = PayrollRecordSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        return PayrollRecord.objects.select_related('employee')

# Additional Views for Common Use Cases
class EmployeesByDepartmentView(generics.ListAPIView):
    """Get all employees in a specific department."""
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        department_id = self.kwargs['department_id']
        return Employee.objects.filter(
            department_id=department_id, 
            status='active'
        ).select_related('department', 'manager')

class EmployeeSubordinatesView(generics.ListAPIView):
    """Get all subordinates of a specific employee."""
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        manager_id = self.kwargs['manager_id']
        return Employee.objects.filter(
            manager_id=manager_id, 
            status='active'
        ).select_related('department')

class PendingLeaveRequestsView(generics.ListAPIView):
    """Get all pending leave requests."""
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LeaveRequest.objects.filter(
            status='pending'
        ).select_related('employee', 'leave_type').order_by('-applied_date')

class EmployeeAttendanceView(generics.ListAPIView):
    """Get attendance records for a specific employee."""
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = {
        'date': ['gte', 'lte', 'exact'],
        'status': ['exact'],
    }
    ordering_fields = ['date']
    ordering = ['-date']

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Attendance.objects.filter(
            employee_id=employee_id
        ).select_related('employee')