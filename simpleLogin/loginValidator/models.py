from django.db import models
from django.forms import ModelForm

class User(models.Model):
	firstName = models.CharField(max_length=30, blank=False, null=False)
	lastName = models.CharField(max_length=30, blank=False, null=False)
	phone = models.CharField(max_length=10, blank=False, null=False)
	address = models.CharField(max_length=70, blank=False, null=False)

	def __str__(self):
		return self.name

# Create your models here.
