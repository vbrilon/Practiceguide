from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.core import dajaxice_autodiscover 
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register
from practice.models import Exercise
import datetime
import re

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
  if key == 'tags':
    tags = (val.split(','))
    # kill whitespace
    tags = [n.strip() for n in tags]
    # Replace newlines with a space
    tags = [re.sub(r'[\n\r]+',' ',n) for n in tags]
    # kill empty entries
    tags = filter(lambda x: not re.match(r'^\s*$', x), tags)
    ex.tags.set(*tags)
  else:
    print "{} set to {}".format(key, val)
    setattr(ex, key, val)
  ex.last_updated = datetime.datetime.now
  ex.save()
  dajax = Dajax()
  dajax.assign('#result','value', "Data saved")
  return dajax.json()
  
