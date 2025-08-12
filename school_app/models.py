from django.db import models
from django.contrib.auth.models import User

#------------------------------------------
#2.Teaching staff model
#------------------------------------------

class Teacher(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.teachers_full_name
    
#------------------------------------------
#2.Students model
#------------------------------------------

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    full_name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    id_number = models.CharField(max_length=20,default=1)
    date_of_birth = models.DateField()
    class_name = models.CharField(max_length=20)
    parent_contact = models.CharField(max_length=15)
    photo = models.ImageField(upload_to='student_photos/', blank=True, null=True)
    total_billed = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    @property
    def is_cleared(self):
        return self.total_paid >= self.total_billed
    
    def __str__(self):
        return f"{self.full_name} ({self.admission_number})"

    
#------------------------------------------
#2.Fees model
#------------------------------------------
class Fee(models.Model):
    students = models.ForeignKey(Student,on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=8,decimal_places=2)
    amount_paid = models.DecimalField(max_digits=8,decimal_places=2)
    date_paid = models.DateField()

    def __str__(self):
        return f'{self.students.full_name}-({self.amount_paid})'
    
class ExamsReport(models.Model):
    students = models.ForeignKey(Student,on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    scores = models.PositiveIntegerField()
    date_exam = models.DateField()

    def __str__(self):
        return f'{self.students.full_name} - ({self.subject}) - ({self.scores})'
    

#----------------------
#2.Roles and user profile
#------------------------
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('teacher', 'Teacher'),
        ('student', 'Student'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

    def __str__(self):
        return f"{self.user.username} ({self.role})"

#-------------------
#5.Exam model
#-------------------
class Exam(models.Model):
    birth_number = models.CharField(max_length=20, unique=True)
    admission_number = models.ForeignKey(Student, on_delete=models.CASCADE)
    unit = models.CharField(max_length=100)
    date = models.DateField()
    total_marks = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.unit} - {self.date} - {self.total_marks} marks"
    
class StudntExamRegestration(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    registration_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.full_name} registered for {self.exam.unit} on {self.registration_date}"