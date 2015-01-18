from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'ssweb.views.hello', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^register/$', 'ssweb.views.register'),
    url(r'^login/$', 'ssweb.views.user_login'),
    url(r'^logout/$', 'ssweb.views.user_logout'),

    url(r'^admin/', include(admin.site.urls)),
)
