from django.conf.urls import patterns, include, url
from django.contrib import admin
import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ssweb.views.hello', name='home'),
    url(r'^register/$', 'ssweb.views.register'),
    url(r'^login/$', 'ssweb.views.user_login'),
    url(r'^logout/$', 'ssweb.views.user_logout'),
    url(r'^user_index/$', 'ssweb.views.user_index'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
)
