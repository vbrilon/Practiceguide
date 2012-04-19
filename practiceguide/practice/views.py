from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404,redirect
from practice.models import Exercise, Session, Performance
from django.template import RequestContext
from practice.forms import *
from user.forms import RegistrationForm
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register
import logging

def edit_exercise(request):
  if request.method == 'GET':
    template = 'exercise/base_view.html'
    return render_to_response(template, request)
  elif request.method == 'POST':
    print "I AM BEING CALLED"
    dajax = Dajax()
    dajax.assign('#result','value', "HELLO WORLD")
    return dajax.json()
  else:
    print "How am I here?"
  
@login_required
def exercises_index(request):
  ex_list = Exercise.objects.filter(user=request.user)
  variables = RequestContext(request, {
     'ex_list': ex_list,
  })
  return render_to_response('exercise.html', variables)

def index(request):
  reg_form = RegistrationForm()
  return render_to_response('index.html', {'reg_form': reg_form}, context_instance=RequestContext(request))

@login_required  
def practice(request, id):
  try:
    e = get_object_or_404(Exercise, pk=id)
  except Exercise.DoesNotExist:
    raise Http404
  if request.user != e.user:
    return HttpResponseForbidden()
  if request.method == 'POST':
    form = ExercisePracticeForm(request.POST)
    if form.is_valid():
      perf = Performance (
        notes = form.cleaned_data['notes'],
        speed = form.cleaned_data['speed'],
        user = request.user,
        rating = form.cleaned_data['choice'],
        exercise = e,
      )
      perf.save()
      return HttpResponseRedirect('/practice/')
  else:
    form = ExercisePracticeForm()
  variables = RequestContext(request, {'form': form})
  return render_to_response('ex_create.html',variables)

  
@login_required
def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

@login_required
def edit_exercise(request, ex=None):
  if ex is None:
    ex = Exercise(
      title = "No Title",
      description = "No Description",
      user = request.user
    )
    ex.save()
  else:
    ex = get_object_or_404(Exercise, pk=ex)
  form = ExerciseCreateModelForm(instance = ex)
  request.session['current_exercise'] = ex.id
  variables = RequestContext(request, {'form': form})
  return render_to_response('exercise/base_view.html',variables)
  
      
