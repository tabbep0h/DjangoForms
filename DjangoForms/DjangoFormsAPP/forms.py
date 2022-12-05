from django import forms

class UserForm(forms.Form):
    name = forms.CharField()
    second_name = forms.CharField()
    email = forms.CharField()
    country = forms.CharField()
    city = forms.CharField()
    street = forms.CharField()
    street_number = forms.IntegerField()
    home_number = forms.IntegerField()