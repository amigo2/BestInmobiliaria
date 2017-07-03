from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.


class Properties(models.Model):

	property_reference = models.CharField(max_length=20)
	title = models.CharField(max_length=250)
	photolink = models.FileField()
	price = models.FloatField();
	description = models.CharField(max_length=1000)

	def get_absolute_url(self):
		#retuirn pk of self 
		return reverse('listing:details',kwargs={'property_id':self.pk})

		

	def __str__(self):
		return self.title + ' - ' + self.description



	

class Demands(models.Model):

	demand_reference = models.CharField(max_length=20)
	client_name = models.CharField(max_length=250)
	phone = models.IntegerField()
	email= models.CharField(max_length=250)
	followUp_blog = models.CharField(max_length=1000)