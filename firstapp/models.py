import functools
from xml.parsers.expat import model
from django.db import models

class ActiveStudManager(models.Manager):
    def get_queryset(self):
        return super(ActiveStudManager,self).get_queryset().filter(is_active=True)

class InactiveStudManager(models.Manager):
    def get_queryset(self):
        return super(InactiveStudManager,self).get_queryset().filter(is_active=False)

# Create your models here.
class Student(models.Model):
   #django automatically create id field 
   name = models.CharField(max_length=100)
   age = models.IntegerField()
   marks = models.FloatField()
   is_active = models.BooleanField(default=True)
   active_objects = ActiveStudManager()
   inactive_objects = InactiveStudManager() 
   objects = models.Manager()
   department = models.ForeignKey("Department", on_delete=models.SET_NULL, null=True)


   class Meta:
       db_table = "student"
     
   def __str__(self):
       return self.name

   def get_stud_details(self):
        print(f""" Student id :-{self.id}
        Student id :-{self.name}
        Student id :-{self.age}
        Student id :-{self.marks}
        """)       
   #---------------------------------------------------------
    #all data
#    @classmethod
#    def get_all_studentsdetails(cls):
#         all_data=cls.objects.all()
    
#         return all_data     

#______-------------------------------------------------------
#    @classmethod
#    def get_avgMark(cls):
#         alldata = cls.objects.all()
#         total = 0
#         for i in alldata:
#             total += i.marks
#         avg = total/len(alldata)
#         return avg    

#-------------------------------------------------------
   @classmethod
   def get_active_stud(cls):
       active_stud = cls.objects.filter(is_active=1)
       return active_stud
#-----------------------# avg_marks_using_lmb()--------------------------  

   @classmethod
   def avg_marks_using_lmb(cls):
        all_data=cls.objects.all()
        l=[]
        for i in all_data:
            l.append(i.marks)
        a = functools.reduce(lambda x,y:x+y,l)
        
        return(a/len(l))

##########################################
class Common_Fields(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True   #It will not create table for this class 

class College(Common_Fields):
    # name = models.CharField(max_length=100)    #we can define the commonfid in common class 
    address = models.CharField(max_length=200)

    class Meta:
        db_table = "college"


class Princi(Common_Fields):
    college = models.OneToOneField(College, on_delete=models.CASCADE, null=True)
    
    class Meta:
        db_table = "princi"


class Department(Common_Fields):
    name = models.CharField(max_length=100, unique=True)
    college = models.ForeignKey(College, on_delete=models.CASCADE, null=True)
    # college = models.ForeignKey(College, on_delete=models.CASCADE, null=True, related_name="dept")
    intake = models.IntegerField(default=60)      

    class Meta:
        db_table="dept"  

class Subject(Common_Fields):
    is_practical = models.BooleanField(default=False)
    total_Marks = models.IntegerField()
    students = models.ManyToManyField(Student)

    class Meta:
        db_table = "subject"


###########################################################################33
class Githubpractic(models.Model):
    firstname = models.CharField(max_length=200)