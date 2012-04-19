import re
from django import forms
from practice.models import Exercise
from django.forms import ModelForm, Textarea

class ExerciseCreateModelForm(ModelForm):
  class Meta: 
    model = Exercise
    fields = ('title', 'description', 'tags', 'instructions', 'media')
    widgets = {
      'tags' : Textarea(),
      'instructions' : Textarea(),
    }

class ExercisePracticeForm(forms.Form):
  notes = forms.CharField(label=u'Practice Notes', widget=forms.Textarea)
  speed = forms.CharField(label=u'Speed Practiced', max_length=3)
  choice = forms.CharField(label=u'How\'d You Do?', widget=forms.Textarea)

