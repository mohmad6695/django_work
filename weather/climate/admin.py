from django.contrib import admin
from .models import *

class Dataadmin(admin.ModelAdmin):
	fields = ['country', 'rainfall', 'tmax','tmin','year','month']
	list_display = ('country', 'rainfall', 'tmax','tmin','year','month')
	list_filter = ['country','year']

admin.site.register(Data, Dataadmin)
