from rest_framework import serializers
from .models import (
    Employee,
    Department,
    Attendance,
    LeaveRequest,
    LeaveType,
    PerformanceReview,
    SalaryHistory,
    PayrollRecord,
)

# Basic serializers for nested representations
class DepartmentBasicSerializer(serializers.ModelSerializer):
    """Basic department serializer for nested use."""
    class Meta:
        model = Department
        fields = ['id', 'name']

class EmployeeBasicSerializer(serializers.ModelSerializer):
    """Basic employee serializer for nested use."""
    full_name = serializers.ReadOnlyField()
    
    class Meta:
        model = Employee
        fields = ['id', 'employee_id', 'full_name', 'email', 'position']

class LeaveTypeBasicSerializer(serializers.ModelSerializer):
    """Basic leave type serializer for nested use."""
    class Meta:
        model = LeaveType
        fields = ['id', 'name', 'days_allowed_per_year']

# Main serializers
class EmployeeSerializer(serializers.ModelSerializer):
    """Serializer for Employee model."""
    full_name = serializers.ReadOnlyField()
    department_name = serializers.CharField(source='department.name', read_only=True)
    manager_name = serializers.CharField(source='manager.full_name', read_only=True)
    
    class Meta:
        model = Employee
        fields = [
            'id', 'employee_id', 'first_name', 'last_name', 'full_name',
            'email', 'phone_number', 'date_of_birth', 'date_hired',
            'position', 'department', 'department_name', 'manager', 
            'manager_name', 'current_salary', 'status'
        ]
        read_only_fields = ['id', 'date_hired']

    def validate_email(self, value):
        """Validate email uniqueness."""
        if Employee.objects.filter(email=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Employee with this email already exists.")
        return value

    def validate_employee_id(self, value):
        """Validate employee_id uniqueness."""
        if Employee.objects.filter(employee_id=value).exclude(id=self.instance.id if self.instance else None).exists():
            raise serializers.ValidationError("Employee with this ID already exists.")
        return value

    def validate(self, data):
        """Custom validation for employee data."""
        # Prevent employee from being their own manager
        if data.get('manager') == self.instance:
            raise serializers.ValidationError("Employee cannot be their own manager.")
        return data

class EmployeeDetailSerializer(EmployeeSerializer):
    """Detailed serializer for Employee with related data."""
    department = DepartmentBasicSerializer(read_only=True)
    manager = EmployeeBasicSerializer(read_only=True)
    subordinates = EmployeeBasicSerializer(many=True, read_only=True)
    
    # Add counts for related objects
    total_leave_requests = serializers.SerializerMethodField()
    pending_leave_requests = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    
    class Meta(EmployeeSerializer.Meta):
        fields = EmployeeSerializer.Meta.fields + [
            'subordinates', 'total_leave_requests', 'pending_leave_requests', 'total_reviews'
        ]
    
    def get_total_leave_requests(self, obj):
        return obj.leave_requests.count()
    
    def get_pending_leave_requests(self, obj):
        return obj.leave_requests.filter(status='pending').count()
    
    def get_total_reviews(self, obj):
        return obj.performance_reviews.count()

class DepartmentSerializer(serializers.ModelSerializer):
    """Serializer for Department model."""
    manager_name = serializers.CharField(source='manager.full_name', read_only=True)
    employee_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Department
        fields = ['id', 'name', 'description', 'manager', 'manager_name', 'employee_count']
        read_only_fields = ['id']
    
    def get_employee_count(self, obj):
        return obj.employees.filter(status='active').count()

class DepartmentDetailSerializer(DepartmentSerializer):
    """Detailed serializer for Department with employees."""
    manager = EmployeeBasicSerializer(read_only=True)
    employees = EmployeeBasicSerializer(many=True, read_only=True)
    
    class Meta(DepartmentSerializer.Meta):
        fields = DepartmentSerializer.Meta.fields + ['employees']

class AttendanceSerializer(serializers.ModelSerializer):
    """Serializer for Attendance model."""
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(source='employee.employee_id', read_only=True)
    
    class Meta:
        model = Attendance
        fields = [
            'id', 'employee', 'employee_name', 'employee_id', 'date',
            'check_in_time', 'check_out_time', 'total_hours', 'status'
        ]
        read_only_fields = ['id', 'total_hours']  # total_hours is calculated automatically

    def validate(self, data):
        """Custom validation for attendance data."""
        check_in = data.get('check_in_time')
        check_out = data.get('check_out_time')
        
        if check_in and check_out and check_in >= check_out:
            raise serializers.ValidationError("Check-out time must be after check-in time.")
        
        return data

class LeaveTypeSerializer(serializers.ModelSerializer):
    """Serializer for LeaveType model."""
    class Meta:
        model = LeaveType
        fields = ['id', 'name', 'days_allowed_per_year', 'description']
        read_only_fields = ['id']

class LeaveRequestSerializer(serializers.ModelSerializer):
    """Serializer for LeaveRequest model."""
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    leave_type_name = serializers.CharField(source='leave_type.name', read_only=True)
    approved_by_name = serializers.CharField(source='approved_by.full_name', read_only=True)
    duration_days = serializers.ReadOnlyField()
    
    class Meta:
        model = LeaveRequest
        fields = [
            'id', 'employee', 'employee_name', 'leave_type', 'leave_type_name',
            'start_date', 'end_date', 'duration_days', 'reason', 'status',
            'approved_by', 'approved_by_name', 'applied_date', 'processed_date'
        ]
        read_only_fields = ['id', 'applied_date', 'processed_date']

    def validate(self, data):
        """Custom validation for leave requests."""
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        
        if start_date and end_date and start_date > end_date:
            raise serializers.ValidationError("Start date cannot be after end date.")
        
        # Check for overlapping leave requests
        employee = data.get('employee')
        if employee and start_date and end_date:
            overlapping = LeaveRequest.objects.filter(
                employee=employee,
                status__in=['pending', 'approved'],
                start_date__lte=end_date,
                end_date__gte=start_date
            )
            
            if self.instance:
                overlapping = overlapping.exclude(id=self.instance.id)
            
            if overlapping.exists():
                raise serializers.ValidationError("This leave request overlaps with an existing request.")
        
        return data

class PerformanceReviewSerializer(serializers.ModelSerializer):
    """Serializer for PerformanceReview model."""
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    reviewer_name = serializers.CharField(source='reviewer.full_name', read_only=True)
    rating_display = serializers.CharField(source='get_rating_display', read_only=True)
    
    class Meta:
        model = PerformanceReview
        fields = [
            'id', 'employee', 'employee_name', 'reviewer', 'reviewer_name',
            'review_period_start', 'review_period_end', 'review_date',
            'rating', 'rating_display', 'goals_achieved', 'areas_of_improvement',
            'comments', 'next_review_date'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """Custom validation for performance reviews."""
        review_period_start = data.get('review_period_start')
        review_period_end = data.get('review_period_end')
        
        if review_period_start and review_period_end and review_period_start > review_period_end:
            raise serializers.ValidationError("Review period start date cannot be after end date.")
        
        # Prevent self-review
        employee = data.get('employee')
        reviewer = data.get('reviewer')
        
        if employee and reviewer and employee == reviewer:
            raise serializers.ValidationError("Employee cannot review themselves.")
        
        return data

class SalaryHistorySerializer(serializers.ModelSerializer):
    """Serializer for SalaryHistory model."""
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(source='employee.employee_id', read_only=True)
    
    class Meta:
        model = SalaryHistory
        fields = [
            'id', 'employee', 'employee_name', 'employee_id', 'amount',
            'effective_date', 'end_date', 'reason', 'created_at'
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        """Custom validation for salary history."""
        effective_date = data.get('effective_date')
        end_date = data.get('end_date')
        
        if effective_date and end_date and effective_date > end_date:
            raise serializers.ValidationError("Effective date cannot be after end date.")
        
        return data

class PayrollRecordSerializer(serializers.ModelSerializer):
    """Serializer for PayrollRecord model."""
    employee_name = serializers.CharField(source='employee.full_name', read_only=True)
    employee_id = serializers.CharField(source='employee.employee_id', read_only=True)
    
    class Meta:
        model = PayrollRecord
        fields = [
            'id', 'employee', 'employee_name', 'employee_id',
            'pay_period_start', 'pay_period_end', 'gross_amount',
            'deductions', 'net_amount', 'payment_date', 'notes'
        ]
        read_only_fields = ['id']

    def validate(self, data):
        """Custom validation for payroll records."""
        pay_period_start = data.get('pay_period_start')
        pay_period_end = data.get('pay_period_end')
        gross_amount = data.get('gross_amount')
        deductions = data.get('deductions', 0)
        net_amount = data.get('net_amount')
        
        if pay_period_start and pay_period_end and pay_period_start > pay_period_end:
            raise serializers.ValidationError("Pay period start date cannot be after end date.")
        
        if gross_amount and deductions and net_amount:
            expected_net = gross_amount - deductions
            if abs(expected_net - net_amount) > 0.01:  # Allow for small rounding differences
                raise serializers.ValidationError("Net amount should equal gross amount minus deductions.")
        
        return data