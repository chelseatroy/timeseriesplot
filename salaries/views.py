from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .regression import predict_salaries
from .models import Employee
from .forms import EmployeeDataForm
import pandas as pd
from io import StringIO

def salaries(request):
    form = EmployeeDataForm()
    return render(request, 'salaries/salaries.html', {'form': form})

def enter_data(request):
    if request.POST and request.FILES:
        form = EmployeeDataForm(request.POST, request.FILES)

        if form.is_valid():
            employee_dataframe = pd.read_csv(request.FILES['employee_info'])

            employees = []
            # employee_data.apply(
            #     employees.append(save_employee_from_row),
            #     axis=0
            # )
            salary_model = predict_salaries(employee_dataframe)
    return HttpResponseRedirect(reverse('salaries:display_coefficients')) #, args=(salary_model.gender_coeff, etc))) #,

def display_coefficients(request):
    return render(request, 'salaries/employee_results.html') #, {'gender_coefficient': gender, 'ethnicity_coefficient': ethnicity}

def save_employee_from_row(employee_row):
    employee = Employee()
    employee.id = employee_row[0]
    employee.ethnicity = employee_row[1]
    employee.gender = employee_row[2]
    employee.age = employee_row[3]
    employee.years_experience = employee_row[4]
    employee.role = employee_row[5]
    return employee

# 2,red,f,12,2,engineer\r2,green,g,14,4,designer\r2,red,f,13,5,engineer\r2,blue,f,12,1,developer\r2,red,g,17,4,developer\r2,green,f,12,4,engineer\r2,red,g,11,2,designer\r