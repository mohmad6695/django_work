from django.core.management.base import BaseCommand
from django.utils import timezone
import urllib
import json
from climate.models import *

class Command(BaseCommand):
	help = 'fetch data from s3'

	def handle(self, *args, **kwargs):

		link1= 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/{0}-{1}.json'
		link2= 'https://s3.eu-west-2.amazonaws.com/interview-question-data/metoffice/Rainfall-England.json'

		country_dict={'UK':'UK', 'ENGLAND':'England', 'SCOTLAND':'Scotland', 'WALES':'Wales'}
		metric_list= ['Tmax', 'Tmin', 'Rainfall']

		for country_key in country_dict.keys():

			country= country_dict[country_key]
			result_list_dict = {}
			final_data ={}
			for metric in metric_list:
				r= urllib.request.urlopen(link1.format(metric,country))
				result_set= json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
				for result in result_set:
					if result['year'] not in final_data.keys():
						final_data[result['year']] = {}
					if result['month'] not in final_data[result['year']].keys():
						final_data[result['year']][result['month']] = {}
					final_data[result['year']][result['month']][metric]=result['value']
			for yearkey in final_data.keys():
				for monthkey in final_data[yearkey].keys():
					d= Data()
					d.country=country_key
					d.year=yearkey
					d.month=monthkey
					d.tmax=final_data[yearkey][monthkey]['Tmax']
					d.tmin=final_data[yearkey][monthkey]['Tmin']
					d.rainfall=final_data[yearkey][monthkey]['Rainfall']
					d.save()




'''
			for result in result_list:

				d= Data()
				d.country=key
				d.year=
				d.month=
				d.tmax=
				d.tmin=
					d.rainfall=
				print(key,metric,data[0])
				'''