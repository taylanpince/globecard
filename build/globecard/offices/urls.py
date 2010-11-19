from django.conf.urls.defaults import *


urlpatterns = patterns('offices.views',
    url(r'^$', 'list', name='offices_list'),
    url(r'^(?P<slug>[-\w]+)/$', 'detail', name='offices_detail'),
)
