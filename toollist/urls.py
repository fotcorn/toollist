from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'toollist.views.home', name='home'),
    url(r'^list/(?P<pk>\d+)/', 'toollist.views.list_tools', name='list_tools'),
    
    url(r'^add_milling/(?P<machine_pk>\d+)/', 'toollist.views.add_milling', name='add_milling'),
    url(r'^edit_milling/(?P<pk>\d+)/', 'toollist.views.edit_milling', name='edit_milling'),
    url(r'^add_turning/(?P<machine_pk>\d+)/', 'toollist.views.add_turning', name='add_turning'),
    url(r'^edit_turning/(?P<pk>\d+)/', 'toollist.views.edit_turning', name='edit_turning'),
    url(r'^remove/(?P<pk>\d+)/', 'toollist.views.remove', name='remove'),
    
    url(r'^chaining/', include('smart_selects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
