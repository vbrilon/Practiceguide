from django import forms
from django.contrib.auth.models import User
#from django.core.validators import validate_email
from django.contrib.auth import login, authenticate

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *


class RegistrationForm(forms.Form):
  first_name = forms.CharField(label='First Name', max_length='75')
  last_name = forms.CharField(label='Last Name', max_length='75')
  email = forms.EmailField(label='Email')
  password1 = forms.CharField(label='Password', widget=forms.PasswordInput())
  password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput())
    
  def clean_password2(self):
    if 'password1' in self.cleaned_data:
      password1 = self.cleaned_data['password1']
      password2 = self.cleaned_data['password2']
      if password1 == password2:
        return password2
        raise forms.ValidationError('Passwords do not match')
  
  def clean_email(self):
    email = self.cleaned_data['email']
    try:
      User.objects.get(email=email)
    except User.MultipleObjectsReturned:
      raise forms.ValidationError("Email already exists")
    except User.DoesNotExist:
      return email
    raise forms.ValidationError("Email already exists")
  
  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.form_id = 'id-registration_form'
    self.helper.form_class = 'form-horizontal'
    self.helper.form_method = 'post'
    self.helper.form_action = '/register/'
    self.helper.add_input(Submit('submit', 'Start practicing for real', css_class='btn btn-primary btn-large'))
    self.helper.add_input(Button('learn', 'Learn more', css_class='btn btn-large'))
    super(RegistrationForm, self).__init__(*args, **kwargs)
        

class LoginForm(forms.Form):
  username = forms.EmailField(label='Email')
  password = forms.CharField(label='Password', widget=forms.PasswordInput())
  
  def clean_password(self):
    user = authenticate(username=self.cleaned_data['username'], password=self.cleaned_data['password'])
    if user is None:
      raise forms.ValidationError("Username and password do not match")
    else:
      return self.cleaned_data['password']
      
  def __init__(self, *args, **kwargs):
    self.helper = FormHelper()
    self.helper.layout = Layout(
      Fieldset(
        'Sign In',
        Field('username'),
        Field('password'),
      )
    )

    self.helper.form_id = 'id-registration_form'
    self.helper.form_class = 'form-horizontal'
    self.helper.form_method = 'post'
    self.helper.form_action = '/login/'
    self.helper.add_input(Submit('submit', 'Sign in', css_class='btn btn-primary'))
    super(LoginForm, self).__init__(*args, **kwargs)
  