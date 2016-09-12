from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.salaries, name='salaries'),
    url(r'^data/$', views.enter_data, name='enter_data'),
    url(r'^results/$', views.display_coefficients, name='display_coefficients'),
]