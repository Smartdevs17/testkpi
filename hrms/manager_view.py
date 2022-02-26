from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg,Sum,Count,OuterRef
from django.contrib.auth import get_user_model
from .models  import (Employee, Department,Kin, Attendance, Leave,SBU_Directorate,
                    Station,Unit,MKPD,SKPD,
                    KPI_Evalutation,KPIScorePenalty,KPIScoreRange,Designation,
                    Employment,GradeLevel,Position,Bank,EmployeeType,KPD,Complaint)
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import FormView, CreateView,View,DetailView,TemplateView,ListView,UpdateView,DeleteView
from .forms import (
    RegistrationForm,
    LoginForm,
    EmployeeForm,
    KinForm,
    DepartmentForm,
    AttendanceForm, 
    LeaveForm,
    EmploymentForm,
    NewEmployeeForm,
    UserForm,
    MKPDForm,
    SKPDForm,
    KPDForm,
    # RatingForm,
    KPI_EvalutationForm,
    ComplaintForm
    )
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin
from datetime import datetime
from datetime import datetime
















# Manager Route

# Manager login
class Manager_Login_View(LoginView):
    # model = get_user_model()
    # model = Manager
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:manager_dashboard')
        return url


class Manager_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:manager_login',permanent=True)




# Manager Board   
class Manager_Dashboard(LoginRequiredMixin,ListView):
    # queryset = Employee.objects.select_related('position')
    # queryset = Employee.objects.get(id=emp_id)
    template_name = 'hrms/manager/managerdashboard.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context['emp_total'] = Employee.objects.all().count()
        context['task_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        # context['workers'] = Employee.objects.order_by('-id')
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        # print(user.dept_name)
        # print(get_object_or_404(Department,head_of_dept__user=self.request.user))
        # print(Employment.objects.filter(department__head_of_dept__user=self.request.user))
        context["manager"] = user
        # context["manager"] = Employment.objects.filter(employee__employee__user=self.request.user)
        # context['project_count'] = Project.objects.all().count()
        # staff = Employment.objects.filter(department=user)
        # print(staff)
        context['staff_total'] = Employment.objects.filter(department=user).count()
        context["staffs"] = Employment.objects.filter(department=user)
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context

# Manager Board   
class Manager_Message_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/messages.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['staff_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context
    
    
# Manager Board   
class Manager_Employee_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/members.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['task_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        user = get_object_or_404(Department,head_of_dept__user=self.request.user)
        context["manager"] = user
        context['staff_total'] = Employment.objects.filter(department=user).count()
        context["staffs"] = Employment.objects.filter(department=user)
        context['tasks'] = MKPD.objects.order_by('-mkpd_id')
        context['projects'] = KPI_Evalutation.objects.order_by('id')
        return context



#   Create Project
class Create_Project_View(LoginRequiredMixin,CreateView):
    model = SKPD
    form_class  = SKPDForm
    manager_url = 'hrms:manager_login'
    template_name = 'hrms/manager/create-project.html'
    success_url = reverse_lazy('hrms:manager_dashboard')
   
    # def dispatch(self,*args,**kwargs):
    #     return super(Create_Project_View,self).dispatch(*args,**kwargs)
    
    def get_form_kwargs(self):
        kwargs = super(Create_Project_View,self).get_form_kwargs()
        kwargs['request'] = self.request
        # kwargs.update({"user":self.request.user})
        return kwargs
    
    # def get_form(self,form_class=None):
    #         form = super(Create_Project_View,self).get_form()
    #         user = get_object_or_404(Department,head_of_dept__user=self.request.user)
    #         form.fields["employee"] = Employment.objects.filter(department=user)
    #         # self.fields['employee'].widget = form.Select()
    #         return form

class Assign_Rating_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/assign-rating-table.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['staff_total'] = MKPD.objects.all().count()
        context['skpd_count'] = SKPD.objects.all().count()
        # rating = SKPD.objects.filter(task_submission__approved="APPROVED").count()
        # print(rating)
        # context["manager"] = Employee.objects.get(position="manager")
        context['projects'] = KPI_Evalutation.objects.order_by('-mkpd_id')
        return context




class Rating_View(LoginRequiredMixin,DetailView):
    model = MKPD
    template_name = 'hrms/manager/project_detail.html'
    login_url = 'hrms:manager_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = MKPD.objects.get(mkpd_id=self.object.pk)
            context["project"] = query
            return context
        except ObjectDoesNotExist:
            return context


class Employee_Report_View(LoginRequiredMixin,DetailView):
    model = Employment
    template_name = 'hrms/manager/employee-report.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = MKPD.objects.get(mkpd_id=self.object.pk)
            context["project"] = query
            return context
        except ObjectDoesNotExist:
            return context

#   KPI EVALUATION
class Evaluation_View(LoginRequiredMixin,CreateView):
    model = KPI_Evalutation
    form_class  = KPI_EvalutationForm
    manager_url = 'hrms:manager_login'
    template_name = 'hrms/manager/kpi_evaluation.html'
    
    success_url = reverse_lazy('hrms:manager_dashboard')
    
    
    # def get_form_kwargs(self):
    #     kwargs = super(Create_Project_View,self).get_form_kwargs()
    #     kwargs['request'] = self.request
    #     return kwargs





class Report_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/reports.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        try:
            # leaders = SKPD.objects.filter(task_submission__approved="APPROVED").annotate(total=Sum("task_submission__score")).order_by("-total")
            leaders = Employment.objects.filter(report__approved="APPROVED").annotate(total=Sum("report__score"))
            tasks = Employment.objects.filter(report__approved="APPROVED").annotate(total=Sum("report__score"))
            # print(tasks[0].report.all())
            # ratings = MKPD.objects.filter(submissions__approved="APPROVED").annotate(Average=Sum("submissions__score"))
            # print(ratings)
            context["kpi_count"] = KPI_Evalutation.objects.all().count()
            # leaders = User.objects.filter(~Q(submissions=None)).filter(submissions__status="approved").annotate(total=Sum("submissions__task__points")).order_by("-total")
            context["employees"] = leaders
            return context
        except ObjectDoesNotExist:
            return context


 # Admin Board   
class Manager_Setting(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/setting.html'
    login_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['reg_total'] = Employment.objects.all().count()
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['manager_count'] = SBU_Directorate.objects.all().count()
        context['station_count'] = Station.objects.all().count()
        context['unit_total'] = Unit.objects.all().count()
        context['grade_total'] = GradeLevel.objects.all().count()
        context['position_total'] = Position.objects.all().count()
        context['bank_total'] = Bank.objects.all().count() 
        context['design_total'] = Designation.objects.all().count()
        context['employeetype_total'] = EmployeeType.objects.all().count()
        context['kpd_total'] = KPD.objects.all().count()
        return context



class Employee_Report_View(LoginRequiredMixin,ListView):
    template_name = 'hrms/manager/reports.html'
    manager_url = 'hrms:manager_login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        try:
            leaders = SKPD.objects.filter(task_submission__approved="APPROVED").annotate(total=Sum("task_submission__score")).order_by("-total")
            # print(leaders)
            context["kpi_count"] = KPI_Evalutation.objects.all().count()
            # leaders = User.objects.filter(~Q(submissions=None)).filter(submissions__status="approved").annotate(total=Sum("submissions__task__points")).order_by("-total")
            context["employees"] = leaders
            return context
        except ObjectDoesNotExist:
            return context




class Employee_Evaluation(CreateView):
    model = KPI_Evalutation  
    form_class = KPI_EvalutationForm  
    # template_name = 'hrms/employee/create.html'
    
    success_url = reverse_lazy('hrms:login')







class Employee_View(LoginRequiredMixin,DetailView):
    template_name = 'hrms/employeedashboard/employeedashboard.html'
    context_object_name = 'employee'
    login_url = 'hrms:login'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context


class Manager_Employee_All(LoginRequiredMixin,ListView):
    template_name = 'hrms/admin/dashboard/employee-all.html'
    model = Employee
    login_url = 'hrms:login'
    model = get_user_model()
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context['reg_total'] = Employment.objects.all().count()
        context['emp_total'] = Employee.objects.all().count()
        context['dept_total'] = Department.objects.all().count()
        context['admin_count'] = get_user_model().objects.all().count()
        context['workers'] = Employment.objects.order_by('employ_id')
        return context

class Manager_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:manager_login',permanent=True)