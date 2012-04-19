from django.utils import simplejson
from dajaxice.core import dajaxice_functions
from dajaxice.core import dajaxice_autodiscover 
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register

dajaxice_autodiscover() 


def myedit(request):
    print "I AM BEING CALLED"
    dajax = Dajax()
    dajax.assign('#result','value', "HELLO WORLD")
    return dajax.json()
dajaxice_functions.register(myedit)

def example1(request):
    """ First simple example """
    return simplejson.dumps({'message': 'hello world'})

dajaxice_functions.register(example1)


def example2(request):
    """ Second simple example """
    return simplejson.dumps({'numbers': [1, 2, 3]})

dajaxice_functions.register(example2)


def example3(request, data, name):
    result = sum(map(int, data))
    return simplejson.dumps({'result': result})

dajaxice_functions.register(example3)


def error_example(request):
    raise Exception("Some Exception")

dajaxice_functions.register(error_example)
