from django.contrib import admin

from .models import Teacher,Student,Fee,ExamsReport

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Fee)
admin.site.register(ExamsReport)

