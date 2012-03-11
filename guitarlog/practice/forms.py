import re
from django import forms
from django.contrib.auth.models import User

class ExerciseCreateForm(forms.Form):
  title = forms.CharField(label=u'Title', max_length=30)
  description = forms.CharField(label=u'Description', max_length=300)
  