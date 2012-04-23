from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os

from django.contrib import admin
admin.autodiscover()
from dajaxice.core import dajaxice_autodiscover
dajaxice_autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')
content = os.path.join(settings.MEDIA_ROOT, 'users')

urlpatterns = patterns('',
  url(r'^$', 'practice.views.index'),
  url(r'^create_exercise/$', 'practice.views.edit_exercise'),
  url(r'^edit_exercise/(?P<ex>\d+)$', 'practice.views.edit_exercise'),
 # url(r'^schedule/$', 'practice.views.schedule'),
#  url(r'^practice/$', 'practice.views.exercises_index'),
 # url(r'^review/$', 'practice.views.review'),
 # url(r'^practice/(?P<id>\d+)/$', 'practice.views.practice'),
 # url(r'^user/(\w+)/$', 'user.views.user_page'),
  url(r'^login/$', 'user.views.mylogin'),
  url(r'^logout/$', 'practice.views.logout_view'),
  url(r'^admin/', include(admin.site.urls)),
  url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
  url(r'^register/$', 'user.views.register_page'),
  url(r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),
  url(r'^exercise_create/success/$', direct_to_template, {'template': 'exercise_create_success.html'}),
  url(r'^%s/' % settings.DAJAXICE_MEDIA_PREFIX, include('dajaxice.urls')),
  url(r'^test/$', direct_to_template, {'template': 'exercise/base_view.html'}),
  url( r'file_upload/$', 'practice.views.upload'),
  url(r'^content/users/(?P<path>.*)$', 'django.views.static.serve', {'document_root': content}),
)
