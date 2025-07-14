from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'hrm'

urlpatterns = [
    # Employee URLs
    path('employees/', views.EmployeeListCreateView.as_view(), name='employee-list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee-detail'),
    path('employees/<int:employee_id>/attendance/', views.EmployeeAttendanceView.as_view(), name='employee-attendance'),
    path('employees/<int:manager_id>/subordinates/', views.EmployeeSubordinatesView.as_view(), name='employee-subordinates'),
    
    # Department URLs
    path('departments/', views.DepartmentListCreateView.as_view(), name='department-list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department-detail'),
    path('departments/<int:department_id>/employees/', views.EmployeesByDepartmentView.as_view(), name='department-employees'),
    
    # Attendance URLs
    path('attendance/', views.AttendanceListCreateView.as_view(), name='attendance-list'),
    path('attendance/<int:pk>/', views.AttendanceDetailView.as_view(), name='attendance-detail'),
    
    # Leave Type URLs
    path('leave-types/', views.LeaveTypeListCreateView.as_view(), name='leavetype-list'),
    path('leave-types/<int:pk>/', views.LeaveTypeDetailView.as_view(), name='leavetype-detail'),
    
    # Leave Request URLs
    path('leave-requests/', views.LeaveRequestListCreateView.as_view(), name='leaverequest-list'),
    path('leave-requests/<int:pk>/', views.LeaveRequestDetailView.as_view(), name='leaverequest-detail'),
    path('leave-requests/pending/', views.PendingLeaveRequestsView.as_view(), name='pending-leave-requests'),
    
    # Performance Review URLs
    path('performance-reviews/', views.PerformanceReviewListCreateView.as_view(), name='performancereview-list'),
    path('performance-reviews/<int:pk>/', views.PerformanceReviewDetailView.as_view(), name='performancereview-detail'),
    
    # Salary History URLs
    path('salary-history/', views.SalaryHistoryListCreateView.as_view(), name='salaryhistory-list'),
    path('salary-history/<int:pk>/', views.SalaryHistoryDetailView.as_view(), name='salaryhistory-detail'),
    
    # Payroll Record URLs
    path('payroll-records/', views.PayrollRecordListCreateView.as_view(), name='payrollrecord-list'),
    path('payroll-records/<int:pk>/', views.PayrollRecordDetailView.as_view(), name='payrollrecord-detail'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)