from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'practice.views.index'),
    url(r'^practice/$', 'practice.views.exercises_index'),
    url(r'^practice/(?P<id>\d+)/$', 'practice.views.exercises'),
    url(r'^user/$', 'practice.views.create_user'),
    # Examples:
    # url(r'^$', 'guitarlog.views.home', name='home'),
    # url(r'^guitarlog/', include('guitarlog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
