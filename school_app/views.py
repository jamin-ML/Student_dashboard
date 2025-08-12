from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Student, UserProfile, StudntExamRegestration
from .forms import  StudentForm,ExamRegistrationForm
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib import messages
def home(request):
    return render(request,'home.html')
def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')
#----------------------
#1.Custom log in
#-------------------
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            profile = UserProfile.objects.get(user=user)
            if profile.role == 'student':
                return redirect('dashboard')
            elif profile.role == 'teacher':
                return redirect('teacher_dashboard')
            elif profile.role == 'admin':
                return redirect('/admin/')  # Django admin
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    messages.success(request, 'You have successfully logged in!')
    
    return render(request, 'login.html')

#------------------------
#Requesting only the user with the role to loog in
#------------------------

def role_required(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            try:
                role = request.user.userprofile.role
                if role in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    return HttpResponseForbidden("Access denied: You do not have permission to view this page.")
            except UserProfile.DoesNotExist:
                return HttpResponseForbidden("No profile found.")
        return wrapper
    return decorator

@login_required
@role_required(allowed_roles=['student'])
def dashboard(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        student = None  # handle case when no profile is found

    return render(request, 'dashboard.html', {'student': student})

@login_required
@role_required(allowed_roles=['teacher'])
def teacher_dashboard(request):
    return render(request, 'dashboards/teacher.html')

def logout_user(request):
    logout(request)
    return redirect('login')

#--------------------
#Register students 
#--------------------
def register_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)

            # Create user
            username = student.admission_number
            password = student.id_number
            user = User.objects.create_user(username=username, password=password)
            student.user = user
            student.save()
            UserProfile.objects.create(user=user, role='student')

            return redirect('student_success')
    else:
        form = StudentForm()

    return render(request, 'register_student.html', {'form': form})

def student_success(request):
    return render(request, 'student_success.html')


@login_required
@role_required(allowed_roles=['student'])
def register_exams(request):
    try:
        student = Student.objects.get(user=request.user)
    except Student.DoesNotExist:
        return HttpResponseForbidden("Student profile not found.")

    if not student.is_cleared:
        return render(request, 'exam_fee_required.html', {'student': student})

    if request.method == 'POST':
        form = ExamRegistrationForm(request.POST)
        if form.is_valid():
            registration, created = StudntExamRegestration.objects.get_or_create(student=request.user)
            registration.exams.set(form.cleaned_data['exams'])
            return redirect('exam_success')
    else:
        form = ExamRegistrationForm()
    
    return render(request, 'exam_register.html', {'form': form})
@login_required
def exam_success(request):
    return render(request, 'exam_success.html')

def about_school(request):
    return render(request, 'about.html')


def academics(request):
    return render(request, 'academic.html')

def admission(request):
    return render(request, 'admission.html')

def contacts(request):
    return render(request, 'contact.html')

def news(request):
    return render(request, 'news.html')