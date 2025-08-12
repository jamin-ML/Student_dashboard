# forms.py
from django import forms
from .models import Student,Exam
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['full_name', 'admission_number', 'id_number', 'date_of_birth', 'class_name', 'parent_contact', 'photo']

class ExamRegistrationForm(forms.Form):
    exams = forms.ModelMultipleChoiceField(
        queryset=Exam.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )
