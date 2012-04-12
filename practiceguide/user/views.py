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
        first_name = form.cleaned_data['first_name'],
        last_name = form.cleaned_data['last_name'],
        username = form.cleaned_data['email'],
        password = form.cleaned_data['password1'],
        email = form.cleaned_data['email'],
       )
      user.save()
      user2 = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password1'])
      login(request, user2)
      return HttpResponseRedirect('/register/success/')
  else:
    return render_to_response('index.html',variables)
