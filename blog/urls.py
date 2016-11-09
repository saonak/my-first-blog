from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.postJ_presentation, name='postJ_presentation'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail2, name='post_detail'),
    url(r'^post/new/$', views.post_new2, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit2, name='post_edit'),
    url(r'^drafts/$', views.post_draft_list2, name='post_draft_list'),
	url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish2, name='post_publish'),
	url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove2, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
    url(r'^title$', views.title_list, name='title_list'),
    url(r'^title/edit/$', views.title_edit, name='title_edit'),
    url(r'^title/err/$', views.title_err, name='title_err'),
    url(r'^postj/presen/$', views.postJ_presentation, name='postJ_presentation'),
    url(r'^postj/(?P<idx>\d+)$', views.postJ_detail, name='postJ_detail'),
    url(r'^postj/(?P<pk>\d+)/edit/$', views.postJ_edit, name='postJ_edit'),
    url(r'^postj/(?P<idx>\d+)/new/$', views.postJ_new, name='postJ_new'),
    url(r'^postj/(?P<pk>\d+)/publish/$', views.postJ_publish, name='postJ_publish'),
	url(r'^postj/(?P<pk>\d+)/remove/$', views.postJ_remove, name='postJ_remove'),
    url(r'^postj/(?P<pk>\d+)/comment/$', views.add_comment_to_postJ, name='add_comment_to_postJ'),
    url(r'^commentj/(?P<pk>\d+)/approve/$', views.commentJ_approve, name='commentJ_approve'),
    url(r'^commentj/(?P<pk>\d+)/remove/$', views.commentJ_remove, name='commentJ_remove'),
]

