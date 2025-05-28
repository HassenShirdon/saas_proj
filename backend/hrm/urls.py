from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.EmployeeList.as_view(), name='employeelist'),
    path('employees/<str:email>/', views.EmployeeDetail.as_view(), name='employee-detail'),
    path('departments/', views.DepartmentList.as_view(), name='departmentlist'),
    path('departments/<str:name>/', views.DepartmentDetail.as_view(), name='department-detail'),
    path('attendance/', views.AttendanceList.as_view(), name='attendancelist'),
    path('attendance/<int:id>/', views.AttendanceDetail.as_view(), name='attendance-detail'),
    path('leaves/', views.LeaveRequestList.as_view(), name='leaverequestlist'),
    path('leaves/<int:id>/', views.LeaveRequestDetail.as_view(), name='leaverequest-detail'),
    path('performance-reviews/', views.PerformanceReviewList.as_view(), name='performancereviewlist'),
    path('performance-reviews/<int:id>/', views.performanceReviewDetail.as_view(), name='performancereview-detail'),
    path('salaries/', views.SalaryList.as_view(), name='salarylist'),
    path('salaries/<int:id>/', views.SalaryDetail.as_view(), name='salary-detail'),

]