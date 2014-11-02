from django.conf.urls import patterns, include, url
from contacts import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ContactList.as_view(), name='contact_list'),
    url(r'^new/$', views.ContactNew.as_view(), name='contact_new'),
    url(
        r'^(?P<contact_id>\d+)/$', 
        views.ContactDetail.as_view(), 
        name='contact_detail'
    ),
    url(
        r'^(?P<contact_id>\d+)/edit/$', 
        views.ContactEdit.as_view(), 
        name='contact_edit'
    ),
)