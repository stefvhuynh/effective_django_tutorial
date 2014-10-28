from django.conf.urls import patterns, include, url

urlpatterns = patterns(
    'contacts.views',
    url(r'^$', 'index', name='index'),
)