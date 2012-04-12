from django import forms
from django.contrib.auth.models import User
#from django.core.validators import validate_email

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


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
    self.helper.form_action = '/register'
    self.helper.add_input(Submit('submit', 'Submit'))
    super(RegistrationForm, self).__init__(*args, **kwargs)
        
