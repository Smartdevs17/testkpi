from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
import time
from datetime import date
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
PERCENTAGE_VALIDATOR = [MinValueValidator(0),MaxValueValidator(100)]
# Create your models here.


# class User(AbstractUser):
#     thumb = models.ImageField()

class Employee(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    email = models.EmailField(max_length=125, null=False)
    dob = models.DateField(max_length=125, null=False)
    mobile = models.CharField(max_length=15)
    nationality = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    country = models.CharField(max_length=15)
    state_of_orgin = models.CharField(max_length=15)
    lga_of_orgin = models.CharField(max_length=15)
    address = models.TextField(max_length=100, default='')
    country_of_residence = models.CharField(max_length=100)
    state_of_residence = models.CharField(max_length=100)
    lga_of_residence = models.CharField(max_length=15)  
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    # department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    account_no = models.CharField(max_length=10, default='')
    bank = models.CharField(max_length=25, default='')

    def __str__(self):
        return self.first_name + " " +self.last_name
    
    # def __str__(self):
    #     return self.user
        
    def get_absolute_url(self):
        return reverse("hrms:employee_login")     
        # return reverse("hrms:employee_view", kwargs={"pk": self.user})   


class EmployeeType(models.Model):
    EMPLOYEETYPE = (('Permanent Staff', 'Permanent Staff'), ('Contract Staff', 'Contract Staff'),('NYSC', 'NYSC'),('SIWES', 'SIWES'),('Freelance', 'Freelance'))
    employee_type_id = models.CharField(max_length=70, primary_key=True,default="emptype"+str(random.randrange(100,999,1)))
    employee_type = models.CharField(choices=EMPLOYEETYPE, max_length=15 )

    def __str__(self):
        return self.employee_type_id

    def get_absolute_url(self):
        return reverse("hrms:employeetype_detail", kwargs={"pk": self.employee_type_id})

class SBU_Directorate(models.Model):
    sbu_id =  models.CharField(max_length=70,primary_key=True,default='sub'+str(random.randrange(100,999,1)))
    sbu_name = models.CharField(max_length=50)
    sbu_email = models.EmailField(max_length=30,null=False)
    director_of_service = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # director_of_service = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.sbu_id


class Department(models.Model):
    dept_id = models.CharField(max_length=70, primary_key=True)
    dept_name = models.CharField(max_length=70, null=False, blank=False)
    head_of_dept = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # head_of_dept = models.CharField(max_length=15,blank=True,null=True)
    description = models.TextField(max_length=1000,null=True,blank=True, default='')
    sbu_id = models.ForeignKey(SBU_Directorate,on_delete=models.SET_NULL, null=True)
    

    def __str__(self):
        return self.dept_name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})

class Unit(models.Model):
    unit_id = models.CharField(max_length=70, primary_key=True,default='unit'+str(random.randrange(100,999,1)))
    head_of_unit = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # head_of_unit = models.CharField(max_length=15,blank=True,null=True)
    dept_id = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.unit_id

class Designation(models.Model):
    design_id = models.CharField(max_length=70, primary_key=True,default='design'+str(random.randrange(100,999,1)))
    designation = models.TextField(max_length=1000,null=True,blank=True, default='')

    def __str__(self):
        return self.design_id


class GradeLevel(models.Model):
    gradelevel_id = models.CharField(max_length=70, primary_key=True,default='gl'+str(random.randrange(100,999,1)))
    # gradelevel = models.IntegerChoices(range(1,17))
    gradelevel = models.IntegerField(choices=[(i,i) for i in range(1,17)], blank=True,null=False)
    
    def __str__(self):
        return self.gradelevel_id

class Position(models.Model):
    position_code = models.CharField(max_length=70, primary_key=True,default='pc'+str(random.randrange(100,999,1)))
    position = models.CharField(max_length=70)
    description = models.TextField(max_length=1000,null=True,blank=True, default='')

    def __str__(self):
        return self.position_code

class Station(models.Model):
    station_id = models.CharField(max_length=70, primary_key=True)
    station_name = models.CharField(max_length=50)
    station_location =  models.TextField(max_length=100, default='')
    station_address =  models.TextField(max_length=100, default='')
    station_email_address = models.EmailField(max_length=30,null=False)
    station_manager = models.ForeignKey(Employee, on_delete=models.CASCADE)
    # station_manager = models.CharField(max_length=15,blank=True,null=True)

    def __str__(self):
        return self.station_id 





class Bank(models.Model):
    bank_id = models.CharField(max_length=70, primary_key=True,default='bank'+str(random.randrange(100,999,1)))
    bank = models.CharField(max_length=150)

    def __str__(self):
        return self.bank_id

class Employment(models.Model):
    employ_id = models.CharField(max_length=70, default='emp'+str(random.randrange(1000,9999,1)))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=25)
    middle_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    doe = models.DateTimeField(default=timezone.now)
    employee_type = models.ForeignKey(EmployeeType,on_delete=models.CASCADE, null=True) 
    sbu_id = models.ForeignKey(SBU_Directorate,on_delete=models.CASCADE, null=True)
    station = models.ForeignKey(Station,on_delete=models.CASCADE, null=True) 
    department = models.ForeignKey(Department,on_delete=models.CASCADE, null=True,related_query_name="dept") 
    unit = models.ForeignKey(Unit,on_delete=models.CASCADE, null=True) 
    designation = models.ForeignKey(Designation,on_delete=models.CASCADE, null=True) 
    grade_level = models.ForeignKey(GradeLevel,on_delete=models.CASCADE, null=True)
    step = models.IntegerField(choices=[(i,i) for i in range(1,16)], blank=True,null=False)
    position =  models.ForeignKey(Position,on_delete=models.CASCADE, null=True)
   

    def __str__(self):
        return self.first_name

class Kin(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    address = models.TextField(max_length=100)
    occupation = models.CharField(max_length=20)
    mobile = models.CharField(max_length=15)
    employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.first_name+'-'+self.last_name
    
    def get_absolute_url(self):
        return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})



class KPD(models.Model):
    # period = models.CharField(max_length=70,default="p:"+str(date.today().month)+":"+str(date.today().year)[-2:])
    sub_id = models.ForeignKey(SBU_Directorate,on_delete=models.CASCADE)
    dept_id = models.ForeignKey(Department,on_delete=models.CASCADE)
    unit_id = models.ForeignKey(Unit, on_delete=models.CASCADE)
    kpd_code = models.AutoField(primary_key=True)
    # date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(max_length=1000,null=True,blank=True, default='')


    def __str__(self):
        return self.description


class KPIScoreRange(models.Model):
    kpiscore_range_id = models.AutoField(primary_key=True)
    kpiscore_range_min = models.IntegerField(choices=[(i,i) for i in range(0,101)], blank=True,null=False)
    kpiscore_range_max = models.IntegerField(choices=[(i,i) for i in range(0,101)], blank=True,null=False)
    kpiscore_remark = models.CharField(max_length=1000,null=True,blank=True, default='')


    def __str__(self):
        return self.kpiscore_remark

class KPIScorePenalty(models.Model):
    kpiscore_penalty_id = models.AutoField(primary_key=True)
    kpiscore_range = models.ForeignKey(KPIScoreRange,on_delete=models.CASCADE)
    percentage_penalty = models.DecimalField(max_digits=3,decimal_places=0,default=float(0),validators=PERCENTAGE_VALIDATOR)
    paybenchmark = models.CharField(max_length=100, default="No Pay Cut")
    
    def __str__(self):
        return self.paybenchmark

class SKPD(models.Model):
    skpd_id = models.AutoField(primary_key=True)
    # name = models.CharField(max_length=100, null=True,blank=True)
    date = models.DateTimeField(auto_now=True)
    WEEK = (('week 1','WEEK 1'),('week 2','WEEK 2'),('week 3','WEEK 3'),('week 4','WEEK 4'))
    week = models.CharField(max_length=15,choices=WEEK)
    sbu = models.ForeignKey(SBU_Directorate,on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employment, on_delete=models.CASCADE,related_name="users")
    kpd = models.ForeignKey(KPD, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=3,decimal_places=0,default=float(0),validators=PERCENTAGE_VALIDATOR)
    expected_time_of_delivery = models.DateField()
    def __str__(self):
        return self.employee.employee.user.username

    def get_absolute_url(self):
        return reverse("hrms:project_detail", kwargs={"pk": self.skpd_id})  
    
class SMKPD(models.Model):
    smkpd_id = models.AutoField(primary_key=True)
    skpdmonth = models.CharField(max_length=50, null=False, blank=True)  
    kpd_id = models.ForeignKey(KPD, on_delete=models.CASCADE)
    perc_weight = models.IntegerField()
    expected_time_of_delivery = models.CharField(max_length=50, null=False, blank=True) 



class MKPD(models.Model):
    mkpd_id = models.AutoField(primary_key=True)
    period = models.CharField(max_length=70,default="p:"+str(date.today().month)+":"+str(date.today().year)[-2:])
    # name = models.CharField(max_length=100, null=True,blank=True)
    employee = models.ForeignKey(Employment, on_delete=models.CASCADE)
    WEEK = (('week 1','WEEK 1'),('week 2','WEEK 2'),('week 3','WEEK 3'),('week 4','WEEK 4'))
    week = models.CharField(max_length=15,choices=WEEK)
    date = models.DateField(null=True)
    description = models.TextField(max_length=1000,null=True,blank=True, default='')
    time_in = models.CharField(max_length=15,null=True)
    time_out = models.CharField(max_length=15,null =True)
    STATUS = (('YES', 'YES'), ('NO', 'NO'))
    approved = models.CharField(max_length=15,choices=STATUS)
    # staff_signed = models.CharField(max_length=15,null=True,blank=True,default='')
    # employee_signed = models.CharField(max_length=15,null=True,blank=True,default='')
    # project_rating = models.IntegerField( blank=True,null=False)
    remark = models.TextField(max_length=1000,null=True,blank=True,default='')

    def __str__(self):
        return self.description
    
    def get_absolute_url(self):
        return reverse("hrms:rating_view", kwargs={"pk": self.mkpd_id})  

# class KPI_Evalutation(models.Model):
#     sbu = models.ForeignKey(Department,on_delete=models.CASCADE)
#     dept = models.ForeignKey(Unit, on_delete=models.CASCADE)
#     # unit = models.OneToOneField(SKPD, on_delete=models.CASCADE)
#     mkpd = models.ForeignKey(MKPD, on_delete=models.CASCADE)
#     skpd = models.ForeignKey(SKPD, on_delete=models.CASCADE)
#     WEEK = (('week 1','WEEK 1'),('week 2','WEEK 2'),('week 3','WEEK 3'),('week 4','WEEK 4'))
#     week = models.CharField(max_length=15,choices=WEEK,null=True,blank=True)   
#     score = models.IntegerField(null=True,blank=False)
#     remark = models.TextField(max_length=1000,null=True,blank=True, default='No Remark')
#     STATUS = (('NOT APPROVED', 'NOT APPROVED'), ('APPROVED', 'APPROVED'))
#     approved = models.CharField(max_length=15,choices=STATUS,default="PENDING")


#     def __str__(self):
#         return str(self.mkpd.employee)

#     def get_absolute_url(self):
#         return reverse("hrms:report_view", kwargs={"pk": self.pk}) 


class KPI_Evalutation(models.Model):
    sbu = models.ForeignKey(Department,on_delete=models.CASCADE)
    dept = models.ForeignKey(Unit, on_delete=models.CASCADE)
    # unit = models.OneToOneField(SKPD, on_delete=models.CASCADE)
    mkpd = models.ForeignKey(MKPD, on_delete=models.CASCADE, related_name="submissions" )
    skpd = models.ForeignKey(SKPD, on_delete=models.CASCADE, related_name="task_submission")
    employee = models.ForeignKey(Employment, on_delete=models.CASCADE, related_name="report")   
    WEEK = (('week 1','WEEK 1'),('week 2','WEEK 2'),('week 3','WEEK 3'),('week 4','WEEK 4'))
    week = models.CharField(max_length=15,choices=WEEK,null=True,blank=True)   
    score = models.IntegerField(null=True,blank=False)
    # remark = models.ForeignKey(KPIScoreRange, on_delete=models.CASCADE, related_name="rating_submission")
    remark = models.CharField(max_length=15,null=True,blank=True)
    COMMENT = (('excellent','EXCELLENT'),('very good','VERY GOOD'),('good','GOOD'),('satisfactory','SATISFACTORY'),('unsatisfactory','UNSATISFACTORY'))  
    comment = models.BooleanField(choices=COMMENT,null=True)
    STATUS = (('NOT APPROVED', 'NOT APPROVED'), ('APPROVED', 'APPROVED'))
    approved = models.CharField(max_length=15,choices=STATUS,default="PENDING")


    def __str__(self):
        return self.employee.employee.user.username

    def get_absolute_url(self):
        return reverse("hrms:report_view", kwargs={"pk": self.pk}) 


class Complaint(models.Model):
    employee = models.ForeignKey(Employment, on_delete=models.CASCADE)   
    STATUS = (('YES', 'YES'), ('NO', 'NO'))
    approved = models.CharField(max_length=15,choices=STATUS)  
    description = models.TextField(max_length=1000,null=True,blank=True, default='')

    def __str__(self):
        return str(self.employee.employee.user)

class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)

    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start





        # <!-- &emsp;<span><a href="{% url 'hrms:employee_view' pk=worker.user %}" class="btn btn-sm btn-info">View</a></span> -->