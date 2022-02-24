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














# Employee View Route
class Employee_Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'hrms/registrations/login.html'

    def get_success_url(self):
        url = resolve_url('hrms:employee_dashboard')
        return url   



class Employee_Logout_View(View):

    def get(self,request):
        logout(self.request)
        return redirect ('hrms:employee_login',permanent=True)

class Employee_Update(LoginRequiredMixin,UpdateView):
    model = Employee
    template_name = 'hrms/employeedashboard/update.html'
    form_class = NewEmployeeForm
    login_url = 'hrms:employeelogin'


class Employee_Dashboard(LoginRequiredMixin,ListView):
    template_name = 'hrms/employeedashboard/employeedashboard.html'
    login_url = 'hrms:employee_login'
    model = Employee
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        # context["employee"] = get_object_or_404(Employee,user=self.request.user) 
        try:
            # print(self.employee)
            # employee = get_object_or_404(Employee,user=self.request.user)
            employee = Employee.objects.get(user=self.request.user)
            # print(employee)
            context["employee"] = Employee.objects.get(user=self.request.user)
            self.employee = Employee.objects.get(user=self.request.user)
            task = SKPD.objects.filter(employee__employee=self.employee)
            # print(task[0].date)
            context["projects"] = SKPD.objects.filter(employee__employee=self.employee)
            context["ratings"] = KPI_Evalutation.objects.filter(skpd__employee__employee=self.employee)
        except ObjectDoesNotExist:
            return context        
        return context


class Employee_Project_Detail(LoginRequiredMixin,DetailView):
    template_name = 'hrms/employeedashboard/todo-tasks.html'
    login_url = 'hrms:employee_login'
    model = Employee
    context_object_name = 'qset'            
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        context["employee"] = get_object_or_404(Employee,user=self.request.user) 
        # context['emp_total'] = Employee.objects.all().count()
        # context['dept_total'] = Department.objects.all().count()
        # context['admin_count'] = get_user_model().objects.all().count()
        # context['workers'] = Employee.objects.order_by('-id')
        try:
            self.employee = get_object_or_404(Employee,user=self.request.user)
            context["employee"] = self.employee = get_object_or_404(Employee,user=self.request.user)
            context["projects"] = SKPD.objects.filter(employee__employee=self.employee)
            context["tasks"] = MKPD.objects.filter(employee__employee=self.employee)

        except ObjectDoesNotExist:
            return context   
  
        return context


#   Create Project
class Complete_Project(LoginRequiredMixin,CreateView):
    model = MKPD
    form_class  = MKPDForm
    login_url = 'hrms:employee_login'
    template_name = 'hrms/employeedashboard/todo-tasks-details.html'

    def form_valid(self,form):
        my_user = Employment.objects.get(employee__user=self.request.user)
        # skpd = SKPD.objects.get(employee__employee__user=self.request.user)
        form.instance.employee = my_user
        # form.instance.skpd = skpd
        return super().form_valid(form)
    success_url = reverse_lazy('hrms:employee_dashboard')

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            query = Kin.objects.get(employee=self.object.pk)
            context["kin"] = query
            return context
        except ObjectDoesNotExist:
            return context

#   Employee Complaint
class Complaint_View(LoginRequiredMixin,CreateView):
    model = Complaint
    form_class  = ComplaintForm
    manager_url = 'hrms:employee_login'
    template_name = 'hrms/employeedashboard/complaint.html'
    
    def form_valid(self,form):
        my_user = Employment.objects.get(employee__user=self.request.user)
        form.instance.employee = my_user
        return super().form_valid(form)    
    
    success_url = reverse_lazy('hrms:employee_dashboard')
    
    
    
    
    
    
    
    
    
    
    





class Employee_New(CreateView):
    model = Employee  
    form_class = EmployeeForm  
    template_name = 'hrms/employee/create.html'
    
    success_url = reverse_lazy('hrms:login')

class New_Employee_View(LoginRequiredMixin,CreateView):
    model = Employee  
    form_class = NewEmployeeForm  
    template_name = 'hrms/employeedashboard/update.html'
    
    def form_valid(self,form):
        my_user = get_user_model().objects.get(username=self.request.user)
        # skpd = SKPD.objects.get(employee__employee__user=self.request.user)
        form.instance.user = my_user
        # form.instance.skpd = skpd
        return super().form_valid(form)
    
    success_url = reverse_lazy('hrms:employee_login')  
    


class Employee_All(LoginRequiredMixin,ListView):
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

        
# class Employee_View(LoginRequiredMixin,DetailView):
#     # queryset = Employee.objects.select_related('department')
#     queryset = Employee.objects.all()
#     # template_name = 'hrms/employee/single.html'
#     template_name = 'hrms/employeedashboard/employeedashboard.html'
#     context_object_name = 'employee'
#     login_url = 'hrms:login'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         try:
#             query = Kin.objects.get(employee=self.object.pk)
#             context["kin"] = query
#             return context
#         except ObjectDoesNotExist:
#             return context


        
# class Employee_Update(LoginRequiredMixin,UpdateView):
#     model = Employee
#     template_name = 'hrms/employee/edit.html'
#     form_class = EmployeeForm
#     login_url = 'hrms:login'
    
    
class Employee_Delete(LoginRequiredMixin,DeleteView):
    pass

class Employee_Kin_Add (LoginRequiredMixin,CreateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_add.html'
    login_url = 'hrms:login'
   

    def get_context_data(self):
        context = super().get_context_data()
        if 'id' in self.kwargs:
            emp = Employee.objects.get(pk=self.kwargs['id'])
            context['emp'] = emp
            return context
        else:
            return context

class Employee_Kin_Update(LoginRequiredMixin,UpdateView):
    model = Kin
    form_class = KinForm
    template_name = 'hrms/employee/kin_update.html'
    login_url = 'hrms:login'

    def get_initial(self):
        initial = super(Employee_Kin_Update,self).get_initial()
        
        if 'id' in self.kwargs:
            emp =  Employee.objects.get(pk=self.kwargs['id'])
            initial['employee'] = emp.pk
            
            return initial