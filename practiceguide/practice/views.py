from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404, HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import logout
from django.shortcuts import render_to_response, get_object_or_404,redirect
from practice.models import Exercise, Session, Performance, Media
from django.template import RequestContext
from practice.forms import *
from user.forms import RegistrationForm
from dajax.core.Dajax import Dajax
from dajaxice.decorators import dajaxice_register
from django.middleware.csrf import get_token
from django.utils import simplejson
from django.conf import settings
from django.core.urlresolvers import reverse
import mimetypes
import logging
import os

mimetypes.init()

def index(request):
  reg_form = RegistrationForm()
  return render_to_response('index.html', {'reg_form': reg_form}, context_instance=RequestContext(request))


  
@login_required
def logout_view(request):
  logout(request)
  return HttpResponseRedirect('/')

@login_required
def edit_exercise(request, ex=None):
  if ex is None:
    ex = Exercise(
      user = request.user
    )
    ex.save()
  else:
    ex = get_object_or_404(Exercise, pk=ex)
  form = ExerciseModelForm(instance = ex)
  request.session['current_exercise'] = ex.id
  csrf_token =  get_token( request )
  variables = RequestContext(request, {'form': form, 'csrf_token': csrf_token})
  return render_to_response('exercise/base_view.html',variables)
  
def upload(request):
  ex = get_object_or_404(Exercise, pk=request.session['current_exercise'])
  f = request.FILES.get('file')
  data = []
  if f is None:
    for f in ex.media.all():
      data.append({'name':  os.path.basename(f.mediafile.name), 'url': settings.MEDIA_URL + f.mediafile.name.replace(" ", "_"), 
      'thumbnail_url': settings.MEDIA_URL + f.mediafile.name.replace(" ", "_"), 
      'delete_url': reverse('upload-delete', args=[f.id]), 'delete_type': "DELETE"})
  else:  
    media = Media(mediafile=f, mediatype=mimetypes.guess_type(f.name))
    media.save()
    ex.media.add(media)
    ex.save()
    data = [{'name':f.name, 'url': settings.MEDIA_URL + "users/" + f.name.replace(" ", "_"), 
      'thumbnail_url': settings.MEDIA_URL + "users/" + f.name.replace(" ", "_"), 
      'delete_url': reverse('upload-delete', args=[media.id]), 'delete_type': "DELETE"}]
  response = JSONResponse(data, {}, response_mimetype(request))
  response['Content-Disposition'] = 'inline; filename=files.json'
  return response

def file_delete(request, pk):
  media = Media.objects.get(pk=pk)
  if media is None:
    print "Can't find that media"
  else:
    media.delete()
    os.remove(os.path.join(settings.MEDIA_ROOT, media.mediafile.name))
  response = JSONResponse(True, {}, response_mimetype(request))
  response['Content-Disposition'] = 'inline; filename=files.json'
  return response
    
  
def response_mimetype(request):
  if "application/json" in request.META['HTTP_ACCEPT']:
    return "application/json"
  else:
    return "text/plain"

  
class JSONResponse(HttpResponse):
  """JSON response class."""
  def __init__(self,obj='',json_opts={},mimetype="application/json",*args,**kwargs):
    content = simplejson.dumps(obj,**json_opts)
    super(JSONResponse,self).__init__(content,mimetype,*args,**kwargs)

