from django import forms


class ProductForm(forms.Form):
    name = forms.CharField(max_length=254)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.IntegerField()
    rating = forms.FloatField()


class ProductFilterForm(forms.Form):
    name = forms.CharField(max_length=254)
    price = forms.IntegerField(required=False)
    rating = forms.FloatField(required=False)


# ModelForm
