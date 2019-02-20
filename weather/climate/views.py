from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from climate.models import Data

# Create your views here


class WeatherView(APIView):
	def get(self, request):
		start_year= request.GET.get('start_year')
		end_year= request.GET.get('end_year')
		start_month= request.GET.get('start_month')
		end_month= request.GET.get('end_month')
		metric= request.GET.get('metric')
		location= request.GET.get('location').upper()


		result_dict = {}
		between_years= Data.objects.filter(year__gt=start_year,year__lt=end_year,country = location)

		start_year_data=Data.objects.filter(year=start_year,month__gte=start_month,country = location)

		end_year_data=Data.objects.filter(year=end_year,month__lte=end_month,country = location)

		for each_data in start_year_data:
			current_date = '%s-%s' %(str(each_data.year),str(each_data.month).zfill(2))
			if metric == 'Tmax':
				result_dict[current_date] = each_data.tmax

			if metric == 'Tmin':
				result_dict[current_date] = each_data.tmin

			if metric == 'Rainfall':
				result_dict[current_date] = each_data.rainfall

		for each_data in between_years:
			current_date = '%s-%s' %(str(each_data.year),str(each_data.month).zfill(2))
			if metric == 'Tmax':
				result_dict[current_date] = each_data.tmax

			if metric == 'Tmin':
				result_dict[current_date] = each_data.tmin

			if metric == 'Rainfall':
				result_dict[current_date] = each_data.rainfall

		for each_data in end_year_data:
			current_date = '%s-%s' %(str(each_data.year),str(each_data.month).zfill(2))
			if metric == 'Tmax':
				result_dict[current_date] = each_data.tmax

			if metric == 'Tmin':
				result_dict[current_date] = each_data.tmin

			if metric == 'Rainfall':
				result_dict[current_date] = each_data.rainfall

		return Response(result_dict)

def index(request):

	start_year= 2000
	end_year= 2004
	start_month= 5
	end_month= 10
	metric= 'Tmax'
	location= 'UK'


	result_dict = {}
	between_years= Data.objects.filter(year__gt=start_year,year__lt=end_year,country = location)

	start_year_data=Data.objects.filter(year=start_year,month__gte=start_month,country = location)

	end_year_data=Data.objects.filter(year=end_year,month__lte=end_month,country = location)

	for each_data in between_years:
		current_date = '%s-%s' %(str(each_data.year),str(each_data.month).zfill(2))
		if metric == 'Tmax':
			result_dict[current_date] = each_data.tmax

		if metric == 'Tmin':
			result_dict[current_date] = each_data.tmin

		if metric == 'Rainfall':
			result_dict[current_date] = each_data.rainfall



	return HttpResponse("bla bla bla")