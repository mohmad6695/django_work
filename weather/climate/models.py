from django.db import models

# Create your models here.
class Data(models.Model):
	COUNTRY_CHOICES = (
		('UK', 'UK'),
		('ENGLAND','ENGLAND'),
		('SCOTLAND', 'SCOTLAND'),
		('WALES', 'WALES')
	)

	MONTH_CHOICES=(
		(1,'JANUARY'),
		(2,'FEBRUARY'),
		(3,'MARCH'),
		(4,'APRIL'),
		(5,'MAY'),
		(6,'JUNE'),
		(7,'JULY'),
		(8,'AUGUST'),
		(9,'SEPTEMBER'),
		(10,'OCTOBER'),
		(11,'NOVEMBER'),
		(12,'DECEMBER')

	)

	country = models.CharField(max_length=20, verbose_name=' Country Name', choices=COUNTRY_CHOICES )
	year = models.IntegerField()
	month= models.IntegerField(choices= MONTH_CHOICES)
	tmax = models.DecimalField(max_digits=5, decimal_places=2)
	tmin = models.DecimalField(max_digits=5, decimal_places=2)
	rainfall = models.DecimalField(max_digits=5, decimal_places=2)
	



	class Meta:

		unique_together = (('country','year','month'),)



	def save(self, *args, **kwargs):

		#check duplicate requests

		try:
			previous_data= Data.objects.get(country= self.country, year= self.year, month= self.month)
			previous_data.tmax= self.tmax
			previous_data.tmin= self.tmin
			previous_data.rainfall= self.rainfall
			previous_data.year= self.year
			previous_data.month= self.month

			super(Data,previous_data).save(*args, **kwargs)
		
		except self.DoesNotExist:

			super(Data,self).save(*args, **kwargs)


	def __str__(self):
		return self.country
