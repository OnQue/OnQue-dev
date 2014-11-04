from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'clients.views.dashboard',),
    url(r'^login/$', 'clients.views.login'),
    url(r'^logout/$', 'clients.views.logout'),
    url(r'^register/$', 'clients.views.register'),
    url(r'^loggedin/$', 'clients.views.dashboard'),
    url(r'^update/$', 'clients.views.update_default'),
    url(r'^api/$', 'clients.views.api'),
    url(r'^waitlist/$', 'clients.views.waitlist'),
    url(r'^checkout/$', 'clients.views.checkout'),
    url(r'^settings/$', 'clients.views.admin_settings'),
    url(r'^dashboard/$', 'clients.views.dashboard'),
    url(r'^add/$', 'clients.views.add'),


    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()