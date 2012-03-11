from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404,redirect
from practice.models import Exercise, Session, Collection, Performance
from django.template import RequestContext
from practice.forms import *


@login_required
def exercises_index(request):
  ex_list = Exercise.objects.filter(user=request.user)
  variables = RequestContext(request, {
     'ex_list': ex_list,
  })
  return render_to_response('exercise.html', variables)

@login_required  
def practice(request, id):
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

@login_required
def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

@login_required
def create_exercise(request):
  if request.method == 'POST':
    form = ExerciseCreateForm(request.POST)
    if form.is_valid():
      ex = Exercise(
        title = form.cleaned_data['title'],
        description = form.cleaned_data['description'],
        user = request.user
       )
      ex.save()
      return HttpResponseRedirect('/exercise_create/success/')
  else:
    form = ExerciseCreateForm()
  variables = RequestContext(request, {'form': form})
  return render_to_response('ex_create.html',variables)
  
      