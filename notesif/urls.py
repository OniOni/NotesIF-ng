from django.conf.urls.defaults import patterns, include, url
import studentapp.urls

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'notesif.views.home', name='home'),
    # url(r'^notesif/', include('notesif.foo.urls')),

    url(r'^', include('notesif.studentapp.urls')),
    (r'^accounts/login/$', 'django_cas.views.login'),
	(r'^accounts/logout/$', 'django_cas.views.logout'),
    
)
