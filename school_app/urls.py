from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from school_app import views  # make sure this is correct
from django.conf import settings
from django.conf.urls.static import static  # for serving media files in development
from django.contrib.auth import views as auth_views


urlpatterns = [ 
    path('',views.home,name='home'),
    path('login/', views.login_user, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_student, name='register_student'),
    path('success/', views.student_success, name='student_success'),
    path('logout/',views.logout_user, name='logout_user'),
    path('register-exams/', views.register_exams, name='register_exams'),
    path('exam-success/', views.exam_success, name='exam_success'),
    path('about-school/', views.about_school, name='about'),
    path('academics/', views.academics, name='academic'),
    path('contact-us/', views.contacts, name='contact'),
    path('admission/', views.admission, name='admission'),
    path('news/', views.news, name='news'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)