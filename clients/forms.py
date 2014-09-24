from tables.models import table
from django import forms
from django.forms import ModelForm

# class MyForm(forms.Form):
# 	n_of_table = forms.IntegerField(required=True)
# 	status = forms.BooleanField(required=True)

class MyForm(forms.ModelForm):
    class Meta:
            model=table
            fields = ['status']

