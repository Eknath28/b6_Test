
from firstapp.models import College, Department, Princi, Student, Subject
# studdata = Student.objects.all()
# print(studdata)
# print(studdata.query)

# f_data = Student.objects.first()
# # print(f_data)

# s_data = Student.objects.filter(id__gte=1)[0]
# print(s_data)
# print(list(s_data), type(s_data))                     #<class 'django.db.models.query.QuerySet'>
# print(list(s_data)[1], type(s_data))                

# single_data = Student.objects.get(id=2)
# single_data = Student.objects.get(id=1)
# print(single_data,type(single_data))     #bbb <class 'firstapp.models.Student'>

# update data

# single_data = Student.objects.get(id=3)
# single_data.name = "CCC"
# single_data.save()
# print(single_data)

# single_data = Student.objects.get(id=1)
# single_data.get_stud_details()   ------method fetching single data
# single_data.name = "AAA"
# single_data.save()
# print(single_data)

# def increment_marks():
#     allmarks = Student.objects.all()
#     for i in allmarks:
#         i.marks += (i.marks*(5/100))
#         if i.marks > 100:
#             continue
#         else:
#             i.save()
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# increment_marks()

# allstd=Student.get_stud_details()
# for i in allstd:
#     print(i)

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# fetching all data 

# allstd=Student.get_all_studentsdetails()
# print(allstd,type(allstd))
# for i in allstd:
#     print(f"""
#             Student Id:- {i.id}
#             Sudent name:-{i.name}
#             Student age"-{i.age}
#             student marks:-{i.marks}
#     """)

#+++++++++++++++++++++++++++++++++++Av marks fun++++++++++++++++++++++++++++++++++++++
# avg = Student.get_avgMark()
# print(avg)

#+++++++++++++++++++++++++++++++++++++==save()
# stud1 = Student(name="FFF", age=13, marks=88)
# stud1.save()

#+++++++++++++++++++++++++++++++++++++++create(return the creatd object)
# stud2 = (Student.objects.create(name="DDD", age=12, marks=90))
# print(stud2)
# stud3 = Student.objects.create(name="EEE", age=11, marks=91)
# print(stud3)

#++++++++++++++++++++++++++++++++++++++++count
# print(Student.objects.count())  
# cnt = len(Student.objects.all())
# print(cnt)

#+++++++++++++++++++++++++++++++++++++++++Ative stud

# print(Student.get_active_stud())
# data = Student.objects.all().filter(is_active=1)
# print(data)

#+++++++++++++++++++++=Custom
# print(Student.active_objects.all())
# print(Student.inactive_objects.all())
# print(Student.objects.all())   #'Student' has no attribute 'objects'  bfore modelManagre

# #+++++++++++++++++++++++++++++++++
# print(Student.avg_marks_using_lmb())

# ++++++++++++++++++++++++++++++++++++++++++++exclude
# print(Student.objects.all().exclude(id__gte=5))

#++++++++++++++++++++order by
# data = Student.objects.all().order_by("name")
# data = Student.objects.all().order_by("-name")
# data = Student.objects.all().order_by("-age")
# print(data)


#############data fetching top to bottom 
c1 = College.objects.get(name="DYPATIL")
# print(c1)
# if college data is not available
# try:
#     c1 = College.objects.get(name="D Y PATIL")
#     print(c1)
# except College.DoesNotExist:
#     print("College does not exist..")
# else:
    # print(c1)  
# print(dir(c1))   

# one to one 
# print(c1.princi)    #Using college object fetching principal name (class name in lower case and in one to one)

# one to many relation(Query set)
# data = c1.department_set.all()
# print(data)

# department se student one to many 

# d1 = Department.objects.get(name="CS")
# print(d1.student_set.all())

# student se subject many to many
# s1 = Student.objects.get(id=1)
# # print(dir(s1))
# print(s1.subject_set.all())

# clg se student fetch 
# dept = c1.department_set.all().filter(name="CS")[0]
# cs_stud = dept.student_set.all()
# print(cs_stud)

# ###################################
# Stud_list = []
# depts = c1.department_set.all()
# for dept in depts:
#     studs=dept.student_set.all()
#     Stud_list.extend(studs)
# print(Stud_list)    

# ##############
# Sub_list = set()
# for stud in Stud_list:
#     subs = stud.subject_set.all()
#     Sub_list.update(subs)
# print(Sub_list)     

##################### reverse direction
# princi name from student
s1 = Student.objects.get(id=3)
# print(s1.department.college.princi)

#clg from student
# print(s1.department.college)

#all department from stud 
# s = Student.objects.all()
# for i in s:
#     print(i.department)

# s2 = Subject.objects.get(id=2)
# print(s2)
# print(dir(s2))

# # subect se Student
# s = Subject.objects.first()
# print(s.students.all())

# s = Subject.objects.first()
# print(s.students.filter(name__istartswith="A"))

# s = Subject.objects.first()
# print(s.students.filter(name__istartswith="E"))


s = Subject.objects.first()
# print(s.students.filter(name__endswith="E"))
# print(s.students.filter(name__icontains="A"))
# print(s.students.filter(name__icontains="X"))  #if no match found will get empty  queryset

# subs = Subject.objects.filter(students__name="AAA")
# print(subs)

# subs = Subject.objects.filter(students__department__name="CS")  #here bydefault is id
# print(subs)


# stud1 = Student.objects.get(name="ccc")
# stud2 = Student.objects.get(name="AAA")
# # Subject.objects.create(name="python", is_practical=True, total_Marks=100)

# s1 = Subject.objects.get(name="python")
# print(s1)

# s1.students.add(stud1,stud2)    #here n add we can pass one or more than one object

# s1.students.remove(stud1) 
# exec(open(r"E:\prog\django pr
# 
# subs = Subject.objects.filter(students__department__college__name="DYPatil").values("total_Marks")  #bydefault id 
# print(subs)

#create college
# c1 = College.objects.create(name="KGKC", address="KARjAT") 
clg = College.objects.get(name="KGKC")
# print(clg)

# p = Princi.objects.create(name="D.Deshmukh", college = clg)
d = Department.objects.create(name="Civil", intake=180, college=clg)

# actice\simple\firstapp\dbshell.py").read())