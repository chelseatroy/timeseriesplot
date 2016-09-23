from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .regression import predict_salaries
from .forms import EmployeeDataForm
import pandas as pd

class WeightsKeeper:
    ordered_weights = "DERP"

def salaries(request):
    form = EmployeeDataForm()
    return render(request, 'salaries/salaries.html', {'form': form})

def enter_data(request):
    if request.POST and request.FILES:
        form = EmployeeDataForm(request.POST, request.FILES)

        if form.is_valid():
            employee_dataframe = pd.read_csv(request.FILES['employee_info'])

            WeightsKeeper.ordered_weights = predict_salaries(employee_dataframe)
    return HttpResponseRedirect(reverse('salaries:display_coefficients'))

def display_coefficients(request):
    weights = WeightsKeeper.ordered_weights
    return render(request, 'salaries/employee_results.html', {'ordered_weights': weights})
