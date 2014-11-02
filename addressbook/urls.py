from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contacts/', include('contacts.urls', namespace='contacts')),
)

urlpatterns += staticfiles_urlpatterns()