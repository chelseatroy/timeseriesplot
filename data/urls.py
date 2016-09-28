from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.data, name='data'),
    url(r'^data/$', views.enter_data, name='enter_data'),
    url(r'^results/$', views.display_results, name='display_results'),
]