from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import DataForm
from .MySeries import MySeries
from matplotlib.backends.backend_agg import FigureCanvasAgg

class DataKeeper:
    series_prediction = MySeries()

def data(request):
    form = DataForm()
    return render(request, 'timeseries/data.html', {'form': form})

def enter_data(request):
    if request.POST and request.FILES:
        form = DataForm(request.POST, request.FILES)

        if form.is_valid():
            # dataframe = pd.read_csv(request.FILES['info'])
            DataKeeper.series_prediction.load_data(request.FILES['info'])  # load in a csv - remember no header!
            DataKeeper.series_prediction.train_model()  # train the model to fit the data
            DataKeeper.series_prediction.make_predictions()

            # DataKeeper.results = predict(dataframe)
    return HttpResponseRedirect(reverse('data:display_results'))

def display_results(request):
    return render(request, 'timeseries/results.html', {'results': None})

def test_matplotlib(request):
    ping = DataKeeper.series_prediction.plot_all()

    canvas = FigureCanvasAgg(ping)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
