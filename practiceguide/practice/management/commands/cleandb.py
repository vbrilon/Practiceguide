from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command 
import os
from django.contrib.auth.models import User

class Command(BaseCommand):
  def handle(self, *args, **options):
    # Nuke existing db
    try:
      os.remove('db/guitarlog.db')
    except os.error:
      pass
    # Build a new one
    call_command('syncdb', interactive=False) 
    
    # Add our content in
    user = User.objects.create_user(
    username = 'a@a.com',
    password = 'a',
    email = 'a',
    )
    user.first_name = 'John'
    user.last_name = 'Petrucci'
    user.save()
