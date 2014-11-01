from django.conf.urls import patterns, include, url
from contacts import views

urlpatterns = patterns(
    '',
    url(r'^$', views.ContactListView.as_view(), name='contact_list'),
    url(r'^new/$', views.ContactFormView.as_view(), name='contact_form'),
    url(
        r'^(?P<contact_id>\d+)/$', 
        views.ContactDetailView.as_view(), 
        name='contact_detail'
    ),
)