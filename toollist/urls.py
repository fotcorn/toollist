from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from toollist import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list/(?P<pk>\d+)/', views.list_tools, name='list_tools'),

    url(r'^add_milling/(?P<machine_pk>\d+)/', views.add_milling, name='add_milling'),
    url(r'^edit_milling/(?P<pk>\d+)/', views.edit_milling, name='edit_milling'),
    url(r'^add_turning/(?P<machine_pk>\d+)/', views.add_turning, name='add_turning'),
    url(r'^edit_turning/(?P<pk>\d+)/', views.edit_turning, name='edit_turning'),
    url(r'^remove/(?P<pk>\d+)/', views.remove, name='remove'),

    url(r'^chaining/', include('smart_selects.urls')),
    path('admin/', admin.site.urls),
]
