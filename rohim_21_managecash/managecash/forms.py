from django import forms
from managecash.models import *

class CashForm(forms.ModelForm):
    class Meta:
        model = CashModel
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = ExpenceModel
        fields = '__all__'
        exclude = ['user']

        widgets = {
            'datetime': forms.DateTimeInput(attrs={'type':'datetime-local'})
        }