from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from OnQueue.api import GuestResource, TableResource, UserResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(GuestResource())
v1_api.register(TableResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'clients.views.dashboard',),
    url(r'^login/$', 'clients.views.login'),
    url(r'^logout/$', 'clients.views.logout'),
    url(r'^register/$', 'clients.views.register'),
    url(r'^loggedin/$', 'clients.views.dashboard'),
    url(r'^update/$', 'clients.views.update_default'),
    url(r'^api_old/$', 'clients.views.api'),
    url(r'^waitlist/$', 'clients.views.waitlist'),
    url(r'^checkout/$', 'clients.views.checkout'),
    url(r'^settings/$', 'clients.views.admin_settings'),
    url(r'^dashboard/$', 'clients.views.dashboard'),
    url(r'^add/$', 'clients.views.add'),
    url(r'^countdown/$', 'clients.views.countdown'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^seated/$', 'clients.views.seated'),
    url(r'^get_waiting_list_of_table/', 'clients.views.get_waiting_list_of_table'),



    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()