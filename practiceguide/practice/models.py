from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm

import datetime

# Create your models here.
class Exercise(models.Model):
	title = models.CharField(max_length=250, blank=False, null=False)
	description = models.CharField(max_length=500, blank=False, null=False)
	user = models.ForeignKey(User)
	class Meta:
		ordering = ['title']
		
	def __str__(self):
		return self.title
				
class Session(models.Model):
	created_date = models.DateTimeField(default=datetime.datetime.now)
	title = models.CharField(max_length=250, blank=False, null=False)
	description = models.CharField(max_length=500, blank=True, null=True)
	notes = models.CharField(max_length=500, blank=True, null=True)
	user = models.ForeignKey(User)
	
class Performance(models.Model):
	created_date = models.DateTimeField(default=datetime.datetime.now)
	rating = models.IntegerField()
	speed = models.IntegerField()
	notes = models.CharField(max_length=500, blank=True, null=True)
	exercise = models.ForeignKey(Exercise)
	user = models.ForeignKey(User)
	
	def __str__(self):
		return self.created_date
		
	class Meta:
		ordering = ['-created_date']
