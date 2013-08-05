from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'toollist.views.home', name='home'),
    url(r'^list/(?P<pk>\d+)/', 'toollist.views.list', name='list'),
    url(r'^edit/(?P<pk>\d+)/', 'toollist.views.edit', name='edit'),
    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
