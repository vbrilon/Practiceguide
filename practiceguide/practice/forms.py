import re
from django import forms
from django.contrib.auth.models import User
from practice.models import Performance


class ExerciseCreateForm(forms.Form):
  title = forms.CharField(label=u'Title', max_length=30)
  description = forms.CharField(label=u'Description', max_length=300)
  
class ExercisePracticeForm(forms.Form):
  notes = forms.CharField(label=u'Practice Notes', widget=forms.Textarea)
  speed = forms.CharField(label=u'Speed Practiced', max_length=3)
  choice = forms.CharField(label=u'How\'d You Do?', widget=forms.Textarea)

