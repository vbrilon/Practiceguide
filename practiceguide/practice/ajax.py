from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.core import dajaxice_autodiscover 
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register

dajaxice_autodiscover() 

@dajaxice_register
def myedit(request, id, val):
    print "I AM BEING CALLED WITH: "
    print "{} -- {}".format(id, val)
    dajax = Dajax()
    dajax.assign('#result','value', "Data saved")
    return dajax.json()
#dajaxice_functions.register(myedit)

