# Create your views here.
from django.http import HttpResponse, Http404
from django.shortcuts import render_to_response, get_object_or_404
from practice.models import Exercise, Session, Collection, Performance

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
	