from django.forms import ModelForm, Textarea
from .models import EmployeeData

class EmployeeDataForm(ModelForm):
    class Meta:
        model = EmployeeData
        fields = ['employee_info']
        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 60})
        }