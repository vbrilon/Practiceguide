# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404,redirect
from practice.models import Exercise, Session, Collection, Performance, UserForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.template import RequestContext



def exercises_index(request):
	ex_list = Exercise.objects.all()
	return render_to_response('exercise.html', {'ex_list': ex_list})
	return HttpResponse("Hello, world. You're at the exercises index")

def exercises(request, id):
	try:
		e = get_object_or_404(Exercise, pk=id)
	except Exercise.DoesNotExist:
		raise Http404
	return HttpResponse("Hello, world. You're at the exercise named: %s" % e.title)
    
def index(request):
	return render_to_response('index.html')
	
def create_user(request):
	form = UserForm(request.POST or None)
	if form.is_valid():
		form.save()
		return render_to_response('user.html', {"form": form, "message": "success"}, context_instance=RequestContext(request))
	
	return render_to_response('user.html', {"form": form}, context_instance=RequestContext(request))
