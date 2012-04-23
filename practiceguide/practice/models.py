from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from taggit.managers import TaggableManager

import datetime

# Create your models here.

class Media(models.Model):
  url = models.URLField(max_length=1024, blank=False, null=False)
  mediafile =  models.FileField(upload_to="users") # this is appended to MEDIA_ROOT
  mediatype = models.CharField(max_length=100, blank=False, null=False)
  name = models.CharField(max_length=100)
  created_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
  class Meta:
    ordering = ['name']    
    def __str__(self):
      return self.name
  		
class Exercise(models.Model):
  title = models.CharField(max_length=250)
  description = models.CharField(max_length=500)
  user = models.ForeignKey(User, blank=False, null=False)
  tags = TaggableManager()
  instructions = models.CharField(max_length=1024)
  media = models.ManyToManyField(Media)
  created_date = models.DateTimeField(auto_now_add=True)
  last_updated = models.DateTimeField(auto_now=True)
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
  last_updated = models.DateTimeField(default=datetime.datetime.now)
  rating = models.IntegerField()
  speed = models.IntegerField()
  notes = models.CharField(max_length=500, blank=True, null=True)
  exercise = models.ForeignKey(Exercise)
  user = models.ForeignKey(User)
  class Meta:
    ordering = ['-created_date']
    def __str__(self):
      return self.created_date
    
