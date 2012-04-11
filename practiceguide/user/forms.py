from django import forms
from django.contrib.auth.models import User
from django.core.validators import validate_email

class RegistrationForm(forms.Form):
  #username = forms.CharField(label=u'Username', max_length=30)
  email = forms.EmailField(label=u'Email')
  password1 = forms.CharField(label=u'Password', widget=forms.PasswordInput())
  password2 = forms.CharField(label=u'Confirm Password', widget=forms.PasswordInput())
    
  def clean_password2(self):
    if 'password1' in self.cleaned_data:
      password1 = self.cleaned_data['password1']
      password2 = self.cleaned_data['password2']
      if password1 == password2:
        return password2
        raise forms.ValidationError('Passwords do not match')
            
  def clean_email(self):
    email = self.cleaned_data['email']
    #if not validate_email(email)
    #  raise forms.ValidationError("Not a valid email address")
    try:
      User.objects.get(email=email)
    except User.MultipleObjectsReturned:
      raise forms.ValidationError("Email already exists")
    except User.DoesNotExist:
      return email
    raise forms.ValidationError("Email already exists")
