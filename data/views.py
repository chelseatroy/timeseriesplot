from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .regression import predict
from .forms import DataForm
import pandas as pd
import matplotlib
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg

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

def test_matplotlib(request):
    f = figure(figsize=(6,6))
    ax = axes([0.1, 0.1, 0.8, 0.8])
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    fracs = [15,30,45, 10]
    explode=(0, 0.05, 0, 0)
    pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
    title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})
    matplotlib.pyplot.close(f)

    canvas = FigureCanvasAgg(f)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
