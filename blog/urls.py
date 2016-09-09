from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list2, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail2, name='post_detail'),
    url(r'^post/new/$', views.post_new2, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit2, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list2, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish2, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove2, name='post_remove'),
]

