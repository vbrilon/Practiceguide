from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.core import dajaxice_autodiscover 
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register
from practice.models import Exercise, Media
from django.conf import settings

import datetime
import re
import os

dajaxice_autodiscover() 
@dajaxice_register
def exedit(request, key, val):
  # fix key to match the attribute
  key = key.replace('id_','')
  try:
    ex = Exercise.objects.get(pk = request.session['current_exercise'])
  except Exercise.DoesNotExist:
    print "ERROR -- Exercise not found in ajax.py"
    print "DEBUG {}".format(request.session['current_exercise'])
  setattr(ex, key, val)
  print "SET: {} - {}".format(key, val)
  ex.last_updated = datetime.datetime.now
  ex.save()
  dajax = Dajax()
  dajax.assign('#result','value', "Data saved")
  return dajax.json()
 
@dajaxice_register
def tag(request, tag, method):
  try:
    ex = Exercise.objects.get(pk = request.session['current_exercise'])
  except Exercise.DoesNotExist:
    print "ERROR -- Exercise not found in ajax.py"
    print "DEBUG {}".format(request.session['current_exercise'])
  if method == "ADD":
    ex.tags.add(tag)
  elif method == "REMOVE":
    ex.tags.remove(tag)
  else:
    print "ERROR -- Unknown method: %s" % method
  dajax = Dajax()
  dajax.assign('#result','value', "Data saved")
  return dajax.json()
