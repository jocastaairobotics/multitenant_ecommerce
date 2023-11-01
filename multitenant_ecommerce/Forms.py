from django import forms


class SearchStudentForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=25, required=False)
    age = forms.IntegerField(min_value=0, max_value=100)
    email = forms.EmailField()
    upload = forms.FileField()
    password = forms.CharField(widget=forms.PasswordInput)
