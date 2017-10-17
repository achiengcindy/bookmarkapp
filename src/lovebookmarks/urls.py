from django.conf.urls import url
from lovebookmarks import views


urlpatterns = [
    
    url(r'^user/(?P<username>[-\w]+)/$', views.bookmark_user, name='lovebookmarks_bookmark_user'),
    #url(r'^user/(?P<username>[\w.@+-]+)/$', views.bookmark_user, name='bookmarksapp.bookmark_user'),
    url(r'^create/$',views.bookmark_create,name='lovebookmarks_bookmark_create'),
    url(r'^edit/(?P<pk>\d+)/$', views.bookmark_edit,name='lovebookmarks_bookmark_edit'),
    url(r'^$', views.bookmark_list, name='lovebookmarks_bookmark_list'),

]
