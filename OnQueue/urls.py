from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'OnQueue.views.index',),
    url(r'^login/$', 'clients.views.login'),
    url(r'^logout/$', 'clients.views.logout'),
    url(r'^register/$', 'clients.views.register'),
    url(r'^loggedin/$', 'clients.views.loggedin'),
    url(r'^update/$', 'clients.views.update_tables'),
    url(r'^api/$', 'clients.views.api'),
    url(r'^waitlist/$', 'clients.views.waitlist'),
    url(r'^checkout/$', 'clients.views.checkout'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
