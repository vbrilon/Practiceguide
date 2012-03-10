# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404,redirect
from practice.models import Exercise, Session, Collection, Performance
from django.template import RequestContext


@login_required
def exercises_index(request):
  ex_list = Exercise.objects.all
  variables = RequestContext(request, {
     'ex_list': ex_list,
  })
  return render_to_response('exercise.html', variables)

  
def exercises(request, id):
  try:
    e = get_object_or_404(Exercise, pk=id)
  except Exercise.DoesNotExist:
    raise Http404
  return HttpResponse("Hello, world. You're at the exercise named: %s" % e.title)
    
def index(request):
  return render_to_response (
  'index.html',
  RequestContext(request)
)

def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')
