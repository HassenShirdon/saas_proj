from rest_framework import serializers
from .models import (
    Employee,
    Department,
    PerformanceReview,
    Attendance,
    LeaveRequest,
    Salary,
)

class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for Employee model."""
    class Meta:
        model = Employee
        fields = '__all__'
        read_only_fields = ['id']

class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for Department model."""
    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id']

class attendanceSerializer(serializers.ModelSerializer):
    """Serializer for Attendance model."""
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['id']

class LeaveRequestSerializer(serializers.ModelSerializer):
    """Serializer for LeaveRequest model."""
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        read_only_fields = ['id']

class PerformanceReviewSerializer(serializers.ModelSerializer):
    """Serializer for PerformanceReview model."""
    class Meta:
        model = PerformanceReview
        fields = '__all__'
        read_only_fields = ['id']

class SalarySerializer(serializers.ModelSerializer):
    """Serializer for Salary model."""
    class Meta:
        model = Salary
        fields = '__all__'
        read_only_fields = ['id']