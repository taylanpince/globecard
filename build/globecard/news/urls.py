from django.conf.urls.defaults import *


urlpatterns = patterns('news.views',
    url(r'^$', 'list', name='news_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail', name='news_detail'),
)
