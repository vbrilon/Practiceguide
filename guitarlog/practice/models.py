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
			
class Collection(models.Model):
	title = models.CharField(max_length=250, blank=False, null=False)
	description = models.CharField(max_length=500, blank=True, null=True)
	user = models.ForeignKey(User)
	
class Session(models.Model):
	created_date = models.DateTimeField(default=datetime.datetime.now)
	title = models.CharField(max_length=250, blank=False, null=False)
	description = models.CharField(max_length=500, blank=True, null=True)
	collection = models.ForeignKey(Collection)
	notes = models.CharField(max_length=500, blank=True, null=True)
	user = models.ForeignKey(User)
	
class Performance(models.Model):
	PERFORMANCE_CHOICES = ((1,'Poor'), (2,'OK'), (3,'Good'),)
	created_date = models.DateTimeField(default=datetime.datetime.now)
	rating = models.IntegerField(choices=PERFORMANCE_CHOICES, default=2)
	speed = models.IntegerField()
	notes = models.CharField(max_length=500, blank=True, null=True)
	exercise = models.ForeignKey(Exercise)
	session = models.ForeignKey(Session)
	user = models.ForeignKey(User)
	
	def __str__(self):
		return self.created_date
		
	class Meta:
		ordering = ['-created_date']
		
class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ["username", "email"]