from django.urls import path

from . import views

urlpatterns = [

	path('get_data', views.index, name= 'index'),
]