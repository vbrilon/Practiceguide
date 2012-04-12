from user.forms import *
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404,redirect
from django.template import RequestContext
from django.contrib.auth import login, authenticate


def register_page(request):
  if request.method == 'POST':
    form = RegistrationForm(request.POST)
    if form.is_valid():
      user = User.objects.create_user(
        username = form.cleaned_data['email'],
        password = form.cleaned_data['password1'],
        email = form.cleaned_data['email'],
       )
      user.first_name = form.cleaned_data['first_name']
      user.last_name = form.cleaned_data['last_name']
      user.save()
      user2 = authenticate(username=form.cleaned_data['email'], password=form.cleaned_data['password1'])
      login(request, user2)
      return HttpResponseRedirect('/register/success/')
    else:
      return render_to_response('index.html', {'reg_form': form}, context_instance=RequestContext(request))

