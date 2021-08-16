from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=100)
	author = models.CharField(max_length=100)
	price = models.IntegerField()
	description = models.TextField()
	image_url = models.CharField(max_length=500)
	buyer = models.ForeignKey(User, default=None, blank = True, on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return f'{self.name}'
