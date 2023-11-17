from django import forms
from .models import Student


# Model Form

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
