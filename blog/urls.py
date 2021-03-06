from django.conf.urls import url
from . import views
from blog.views import PostJDelete, TitleDelete, ExpertDelete, PresenDelete, TestDelete

urlpatterns = [
    url(r'^$', views.presen_detail, name='presen_detail'),
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
    url(r'^title/new/$', views.title_new, name='title_new'),
    url(r'^title/(?P<pk>\d+)/edit/$', views.title_edit, name='title_edit'),
    url(r'^title/(?P<pk>\d+)/delete/$', TitleDelete.as_view(), name='title_deleteview'),
    url(r'^title/(?P<pk>\d+)/remove/$', views.title_remove, name='title_remove'),
    url(r'^title/err/$', views.title_err, name='title_err'),
    url(r'^expert$', views.expert_list, name='expert_list'),
    url(r'^expert/new/$', views.expert_new, name='expert_new'),
    url(r'^expert/(?P<pk>\d+)/edit/$', views.expert_edit, name='expert_edit'),
    url(r'^expert/(?P<pk>\d+)/delete/$', ExpertDelete.as_view(), name='expert_deleteview'),
    url(r'^expert/(?P<pk>\d+)/remove/$', views.expert_remove, name='expert_remove'),
    url(r'^postj/(?P<idx>\d+)$', views.postJ_detail, name='postJ_detail'),
    url(r'^postj/(?P<pk>\d+)/edit/$', views.postJ_edit, name='postJ_edit'),
    url(r'^postj/(?P<idx>\d+)/new/$', views.postJ_new, name='postJ_new'),
    url(r'^postj/(?P<pk>\d+)/publish/$', views.postJ_publish, name='postJ_publish'),
    url(r'^postj/(?P<pk>\d+)/delete/$', PostJDelete.as_view(), name='postj_deleteview'),
    url(r'^postj/(?P<pk>\d+)/remove/$', views.postJ_remove, name='postJ_remove'),
    url(r'^postj/(?P<pk>\d+)/comment/$', views.add_comment_to_postJ, name='add_comment_to_postJ'),
    url(r'^commentj/(?P<pk>\d+)/approve/$', views.commentJ_approve, name='commentJ_approve'),
    url(r'^commentj/(?P<pk>\d+)/remove/$', views.commentJ_remove, name='commentJ_remove'),
    url(r'^presen/$', views.presen_detail, name='presen_detail'),
    url(r'^presen/(?P<pk>\d+)/edit/$', views.presen_edit, name='presen_edit'),
    url(r'^presen/new/$', views.presen_new, name='presen_new'),
    url(r'^presen/(?P<pk>\d+)/publish/$', views.presen_publish, name='presen_publish'),
    url(r'^presen/(?P<pk>\d+)/delete/$', PresenDelete.as_view(), name='presen_deleteview'),
    url(r'^presen/(?P<pk>\d+)/remove/$', views.presen_remove, name='presen_remove'),
    url(r'^presen/(?P<pk>\d+)/comment/$', views.add_comment_to_presen, name='add_comment_to_presen'),
    url(r'^commentP/(?P<pk>\d+)/approve/$', views.commentP_approve, name='commentP_approve'),
    url(r'^commentP/(?P<pk>\d+)/remove/$', views.commentP_remove, name='commentP_remove'),
    url(r'^test/(?P<kind>\d+)/test$', views.test_detail, name='test_detail'),
    url(r'^test/(?P<pk>\d+)/edit/$', views.test_edit, name='test_edit'),
    url(r'^test/(?P<kind>\d+)/new/$', views.test_new, name='test_new'),
    url(r'^test/(?P<pk>\d+)/publish/$', views.test_publish, name='test_publish'),
    url(r'^test/(?P<pk>\d+)/delete/$', TestDelete.as_view(), name='test_deleteview'),
    url(r'^test/(?P<pk>\d+)/remove/$', views.test_remove, name='test_remove'),
]

