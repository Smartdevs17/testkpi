from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.db.models import Avg,Sum,Count
from django.contrib.auth import get_user_model
from .models  import Employee, Department,Kin, Attendance, Leave,SBU_Directorate,Station,Unit,MKPD,SKPD,KPI_Evalutation,KPIScorePenalty,KPIScoreRange,EmployeeType,Designation,Bank,GradeLevel,Position,Station,KPIScoreRange,KPIScorePenalty,Employment,KPD
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
    EmployeeTypeForm,
    DirectorateForm,
    UnitForm,
    DesignationForm,
    BankForm,
    GradeLevelForm,
    PositionForm,
    StationForm,
    KPIScoreRangeForm,
    KPIScorePenaltyForm,
    )
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from braces.views import LoginRequiredMixin,SuperuserRequiredMixin




#EmployeeType views

class EmployeeType_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class EmployeeType_New (LoginRequiredMixin,CreateView):
    model = EmployeeType
    template_name = 'hrms/admin/component/add-employeetype.html'
    form_class = EmployeeTypeForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:admin_setting')

class EmployeeType_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class EmployeeType_Delete(LoginRequiredMixin,DeleteView):
    pass





#SBU_DIRECTORATE views

class Directorate_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Directorate_New (LoginRequiredMixin,CreateView):
    model = SBU_Directorate
    template_name = 'hrms/admin/component/add-sbu.html'
    form_class = DirectorateForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Directorate_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Directorate_Delete(LoginRequiredMixin,DeleteView):
    pass


#Department views

class Department_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Department_New (LoginRequiredMixin,CreateView):
    model = Department
    template_name = 'hrms/admin/component/add-dept.html'
    form_class = DepartmentForm
    login_url = 'hrms:login'
    
    success_url = reverse_lazy('hrms:admin_setting')

class Department_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = DepartmentForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:admin_dashboard')




#Station views

class Station_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Station.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Station.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Station_New (LoginRequiredMixin,CreateView):
    model = Station
    template_name = 'hrms/admin/component/add-station.html'
    form_class = StationForm
    login_url = 'hrms:login'
    
    success_url = reverse_lazy('hrms:admin_setting')

class Station_Update(LoginRequiredMixin,UpdateView):
    model = Department
    template_name = 'hrms/department/edit.html'
    form_class = StationForm
    login_url = 'hrms:admin_login'
    success_url = reverse_lazy('hrms:admin_dashboard')

#Unit views

class Unit_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employee.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Department.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Unit_New (LoginRequiredMixin,CreateView):
    model = Unit
    template_name = 'hrms/admin/component/add-unit.html'
    form_class = UnitForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Unit_Update(LoginRequiredMixin,UpdateView):
    model = Unit
    template_name = 'hrms/department/edit.html'
    form_class = UnitForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Unit_Delete(LoginRequiredMixin,DeleteView):
    pass





#Designation views
class Designation_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Designation.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Designation.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Designation_New (LoginRequiredMixin,CreateView):
    model = Unit
    template_name = 'hrms/admin/component/add-design.html'
    form_class = DesignationForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Designation_Update(LoginRequiredMixin,UpdateView):
    model = Designation
    template_name = 'hrms/department/edit.html'
    form_class = DesignationForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Designation_Delete(LoginRequiredMixin,DeleteView):
    pass



#GradeLevel views
class GradeLevel_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = GradeLevel.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Designation.objects.get(pk=self.kwargs['pk']) 
        return context
    
class GradeLevel_New (LoginRequiredMixin,CreateView):
    model = GradeLevel
    template_name = 'hrms/admin/component/add-gradelevel.html'
    form_class = GradeLevelForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:admin_setting')

class GradeLevel_Update(LoginRequiredMixin,UpdateView):
    model = GradeLevel
    template_name = 'hrms/department/edit.html'
    form_class = GradeLevelForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class GradeLevel_Delete(LoginRequiredMixin,DeleteView):
    pass


#Position views
class Position_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Position.objects.filter(department=self.kwargs['pk'])
        return queryset
    success_url = reverse_lazy('hrms:admin_dashboard')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Position.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Position_New (LoginRequiredMixin,CreateView):
    model = Position
    template_name = 'hrms/admin/component/add-position.html'
    form_class = PositionForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Position_Update(LoginRequiredMixin,UpdateView):
    model = Position
    template_name = 'hrms/department/edit.html'
    form_class = PositionForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Position_Delete(LoginRequiredMixin,DeleteView):
    pass







#Bank views
class Bank_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Bank.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Bank.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Bank_New (LoginRequiredMixin,CreateView):
    model = Bank
    template_name = 'hrms/admin/component/add-bank.html'
    form_class = BankForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Bank_Update(LoginRequiredMixin,UpdateView):
    model = Bank
    template_name = 'hrms/department/edit.html'
    form_class = BankForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Bank_Delete(LoginRequiredMixin,DeleteView):
    pass




#Position views
class KPD_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = KPD.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = KPD.objects.get(pk=self.kwargs['pk']) 
        return context
    
class KPD_New (LoginRequiredMixin,CreateView):
    model = KPD
    template_name = 'hrms/manager/add-kpd.html'
    form_class = KPDForm
    login_url = 'hrms:manager_login'

    success_url = reverse_lazy('hrms:manager_setting')

class KPD_Update(LoginRequiredMixin,UpdateView):
    model = KPD
    template_name = 'hrms/department/edit.html'
    form_class = KPDForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class KPD_Delete(LoginRequiredMixin,DeleteView):
    pass


#KPIScoreRange  views
class KPIScoreRange_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = KPIScoreRange.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = KPIScoreRange.objects.get(pk=self.kwargs['pk']) 
        return context
    
class KPIScoreRange_New (LoginRequiredMixin,CreateView):
    model = Position
    template_name = 'hrms/admin/component/add-kpiscore-range.html'
    form_class = KPIScoreRangeForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:admin_setting')

class KPIScoreRange_Update(LoginRequiredMixin,UpdateView):
    model = KPIScoreRange
    template_name = 'hrms/department/edit.html'
    form_class = KPIScoreRangeForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class KPIScoreRange_Delete(LoginRequiredMixin,DeleteView):
    pass



#Employmentviews
class Employment_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = Employment.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = Employment.objects.get(pk=self.kwargs['pk']) 
        return context
    
class Employment_New (LoginRequiredMixin,CreateView):
    model = Employment
    template_name = 'hrms/admin/component/add-employment.html'
    form_class = EmploymentForm
    login_url = 'hrms:admin_login'

    success_url = reverse_lazy('hrms:admin_setting')

class Employment_Update(LoginRequiredMixin,UpdateView):
    model = Employment
    template_name = 'hrms/department/edit.html'
    form_class = EmploymentForm
    login_url = 'hrms:login'
    success_url = reverse_lazy('hrms:dashboard')


class Employment_Delete(LoginRequiredMixin,DeleteView):
    pass



#Employmentviews
class Evaluation_Detail(LoginRequiredMixin, ListView):
    context_object_name = 'employees'
    template_name = 'hrms/department/single.html'
    login_url = 'hrms:login'
    def get_queryset(self): 
        queryset = KPI_Evalutation.objects.filter(department=self.kwargs['pk'])
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["dept"] = KPI_Evalutation.objects.get(pk=self.kwargs['pk']) 
        return context
    
# class Evaluation_New (LoginRequiredMixin,CreateView):
#     model = Employment
#     template_name = 'hrms/admin/component/add-employment.html'
#     form_class = KPI_EvalutationForm
#     login_url = 'hrms:admin_login'

#     success_url = reverse_lazy('hrms:admin_setting')

class Evaluation_Update(LoginRequiredMixin,UpdateView):
    model = KPI_Evalutation
    me = 'hrms/manager/coomponents/edit-kpi.html'
    form_class = KPI_EvalutationForm
    login_url = 'hrms:manager_login'
    success_url = reverse_lazy('hrms:manager_dashboard')


class Evaluation_Delete(LoginRequiredMixin,DeleteView):
    pass