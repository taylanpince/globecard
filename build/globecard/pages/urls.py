from django.conf.urls.defaults import *


urlpatterns = patterns('pages.views',
    url(r'^(?P<section>[-\w]+)/$', 'landing', name='pages_section'),
    url(r'^(?P<section>[-\w]+)/(?P<slug>[-\w]+)/$', 'detail', name='pages_detail'),
)
