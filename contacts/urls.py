from django.conf.urls import patterns, include, url
from contacts import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ContactList.as_view(), name='contact_list'),
)