from django.urls import path
from . import views
app_name = 'hrms'


urlpatterns = [
    # Authentication Routes
    # path("",views.index,name="index"),
    path('', views.Index.as_view(), name='index'),
    path('register/', views.Register.as_view(), name='reg'),
    path('login/', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),
    path('dashboard/', views.Dashboard.as_view(), name='dashboard'),
    path('dashboard/employee/new/', views.New_Employee_View.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/update/',views.Employee_Update.as_view(), name='employee_update'),



      # Admin Routes
    path('admin_login/', views.Admin_Login_View.as_view(), name='admin_login'),
    path('admin_dashboard/', views.Admin_Dashboard.as_view(), name='admin_dashboard'),
    path('admin_dashboard/settings', views.Admin_Setting.as_view(), name='admin_setting'),
    path('admin_logout/', views.Admin_Logout_View.as_view(), name='admin_logout'),
    path("admin_dashboard/report_complaint",views.Complaint_Report.as_view(), name ="report_complaint"),


     # Manager Routes
    path('manager_login/', views.Manager_Login_View.as_view(), name='manager_login'),
    path('manager_messages/', views.Manager_Message_View.as_view(), name='manager_message'),
    path('manager_dashboard/', views.Manager_Dashboard.as_view(), name='manager_dashboard'),
    path('manager_create_project/', views.Create_Project_View.as_view(), name='create_project'),
    path('manager_assgin_rating/', views.Assign_Rating_View.as_view(), name='assign_rating'),
    path('manager_dashboard/project_rating/<int:pk>/view/', views.Rating_View.as_view(), name='rating_view'),
    path('manager/kpi_evaluation/', views.Evaluation_View.as_view(), name='evaluation'),
    path('manager/report/', views.Report_View.as_view(), name='manager_report'),
    # path('manager_dashboard/<int:pk>/view/', views.Manager_Dashboard.as_view(), name='manager_dashboard'),
    path('manager_dashboard/settings', views.Manager_Setting.as_view(), name='manager_setting'),
    path('manager_logout/', views.Manager_Logout_View.as_view(), name='manager_logout'),




# New Employee Routes
    path('employee_login/', views.Employee_Login_View.as_view(), name='employee_login'),
    path('employee_dashboard/', views.Employee_Dashboard.as_view(), name='employee_dashboard'),
    path('employee_dashboard/<int:pk>/project_detial/', views.Employee_Project_Detail.as_view(), name='project_detail'),
    path('employee_complete_task/', views.Complete_Project.as_view(), name='complete_task'),
    # path('employee_dashboard/project/<int:pk>/detial/', views.Project_Detail_View.as_view(), name='project_detail'),
    path('employee_report/<int:pk>/view/', views.Employee_Report_View.as_view(), name='report_view'),
    path('employee_logout/', views.Employee_Logout_View.as_view(), name='employee_logout'),
    path('employee_complaint/', views.Complaint_View.as_view(), name='employee_complaint'),


# Employee Routes
    path('dashboard/employee/', views.Employee_All.as_view(), name='employee_all'),
    # path('dashboard/employee/new/', views.Employee_New.as_view(), name='employee_new'),
    path('dashboard/employee/<int:pk>/view/', views.Employee_View.as_view(), name='employee_view'),
    # path('dashboard/employee/<int:pk>/update/', views.Employee_Update.as_view(), name='employee_update'),
    path('dashboard/employee/<int:pk>/delete/', views.Employee_Delete.as_view(), name='employee_delete'),
    path('dashboard/employee/<int:id>/kin/add/', views.Employee_Kin_Add.as_view(), name='kin_add'),
    path('dashboard/employee/<int:id>/kin/<int:pk>/update/', views.Employee_Kin_Update.as_view(), name='kin_update'),


# #EmployeeType Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/employeetype/add/', views.EmployeeType_New.as_view(), name='employeetype_new'),
#     path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
#     path('dashboard/employee/<str:pk>/delete/', views.EmployeeType_Delete.as_view(), name='employee_delete'),


# #EmployeeType Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/directorate/add/', views.Directorate_New.as_view(), name='directorate_new'),
#     path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),
#     path('dashboard/employee/<str:pk>/delete/', views.EmployeeType_Delete.as_view(), name='employee_delete'),

    path('dashboard/employeetype/add/', views.EmployeeType_New.as_view(), name='employeetype_new'),
    path('dashboard/directorate/add/', views.Directorate_New.as_view(), name='directorate_new'),
    path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/unit/add/', views.Unit_New.as_view(), name='unit_new'),
    path('dashboard/designation/add/', views.Designation_New.as_view(), name='design_new'),
    path('dashboard/gradelevel/add/', views.GradeLevel_New.as_view(), name='grade_new'),
    path('dashboard/position/add/', views.Position_New.as_view(), name='position_new'),
    path('dashboard/station/add/', views.Station_New.as_view(), name='station_new'),
    path('dashboard/bank/add/', views.Bank_New.as_view(), name='bank_new'),
    path('dashboard/employment/add/', views.Employment_New.as_view(), name='employment_new'),
    path('dashboard/kpd/add/', views.KPD_New.as_view(), name='kpd_new'),
    path('dashboard/kpiscorerange/add/', views.KPIScoreRange_New.as_view(), name='kpiscore_new'),


# #Department Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
#     path('dashboard/department/<int:pk>/update/', views.Department_Update.as_view(), name='dept_update'),


# #Department Routes
#     path('dashboard/department/<int:pk>/', views.Department_Detail.as_view(), name='dept_detail'),
#     path('dashboard/department/add/', views.Department_New.as_view(), name='dept_new'),
    path('dashboard/kpi_evaluation/<int:pk>/update/', views.Evaluation_Update.as_view(), name='evaluation_update'),



#Attendance Routes
    path('dashboard/attendance/in/', views.Attendance_New.as_view(), name='attendance_new'),
    path('dashboard/attendance/<int:pk>/out/', views.Attendance_Out.as_view(), name='attendance_out'),

#Leave Routes

    path("dashboard/leave/new/", views.LeaveNew.as_view(), name="leave_new"),

#Recruitment

    # path("recruitment/",views.RecruitmentNew.as_view(), name="recruitment"),
    # path("recruitment/all/",views.RecruitmentAll.as_view(), name="recruitmentall"),
    # path("recruitment/<int:pk>/delete/", views.RecruitmentDelete.as_view(), name="recruitmentdelete"),

#Payroll
    path("employee/pay/",views.Pay.as_view(), name="payroll")
]
