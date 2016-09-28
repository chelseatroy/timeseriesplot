from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .regression import predict
from .forms import DataForm
import pandas as pd

class DataKeeper:
    results = "DERP"

def data(request):
    form = DataForm()
    return render(request, 'timeseries/data.html', {'form': form})

def enter_data(request):
    if request.POST and request.FILES:
        form = DataForm(request.POST, request.FILES)

        if form.is_valid():
            dataframe = pd.read_csv(request.FILES['info'])

            DataKeeper.results = predict(dataframe)
    return HttpResponseRedirect(reverse('data:display_results'))

def display_results(request):
    results = DataKeeper.results
    return render(request, 'timeseries/results.html', {'results': results})
