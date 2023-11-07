from django import forms


class ProductForm(forms.Form):
    kanif = forms.CharField(max_length=254)
    santoshi = forms.CharField(widget=forms.Textarea)
    niraj = forms.IntegerField()
    pratik = forms.FloatField()
