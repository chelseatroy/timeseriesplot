from django import forms
from .models import Data

class DataForm(forms.Form):
    info = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )