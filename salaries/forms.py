from django import forms
from .models import EmployeeData

class EmployeeDataForm(forms.Form):
    employee_info = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )