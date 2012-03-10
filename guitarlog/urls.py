from django.views.generic.simple import direct_to_template
from django.conf.urls.defaults import patterns, include, url
import os

from django.contrib import admin
admin.autodiscover()

site_media = os.path.join(os.path.dirname(__file__), 'site_media')

urlpatterns = patterns('',
	url(r'^$', 'practice.views.index'),
    url(r'^practice/$', 'practice.views.exercises_index'),
    url(r'^practice/(?P<id>\d+)/$', 'practice.views.exercises'),
    url(r'^user/(\w+)/$', 'user.views.user_page'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'practice.views.logout_view'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': site_media}),
    url(r'^register/$', 'user.views.register_page'),
    url(r'^register/success/$', direct_to_template, {'template': 'registration/register_success.html'}),
)
