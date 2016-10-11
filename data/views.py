from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import DataForm
from .MySeries import MySeries
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from pylab import figure, axes, pie, title
from matplotlib.backends.backend_agg import FigureCanvasAgg

class DataKeeper:
    apple = MySeries()

def data(request):
    form = DataForm()
    return render(request, 'timeseries/data.html', {'form': form})

def enter_data(request):
    if request.POST and request.FILES:
        form = DataForm(request.POST, request.FILES)

        if form.is_valid():
            # dataframe = pd.read_csv(request.FILES['info'])
            DataKeeper.apple.load_data(request.FILES['info'])  # load in a csv - remember no header!
            DataKeeper.apple.train_model()  # train the model to fit the data
            DataKeeper.apple.make_predictions()

            # DataKeeper.results = predict(dataframe)
    return HttpResponseRedirect(reverse('data:display_results'))

def display_results(request):
    return render(request, 'timeseries/results.html', {'results': None})

def test_matplotlib(request):
    ping = DataKeeper.apple.plot_all()

    canvas = FigureCanvasAgg(ping)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
