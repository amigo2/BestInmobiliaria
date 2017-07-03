from django.db import models

# Create your models here.


class Stock(models.Model):
	
	ticker = models.CharField(max_length=10)
	openMarket = models.FloatField()
	closeMarket = models.FloatField()
	volume = models.IntegerField()

	def __str__(self):

		return self.ticker


