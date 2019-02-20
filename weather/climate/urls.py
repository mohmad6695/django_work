from django.urls import path

from . import views


urlpatterns = [

	path('get_data', views.WeatherView.as_view(), name= 'index'),
]