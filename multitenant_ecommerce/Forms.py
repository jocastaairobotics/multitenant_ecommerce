from django import forms


class SearchStudentForm(forms.Form):
    name = forms.CharField(max_length=50)
    surname = forms.CharField(max_length=25, required=False)
