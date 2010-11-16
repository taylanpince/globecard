from django.conf.urls.defaults import *


urlpatterns = patterns('locations.views',
    url(r'^$', 'landing', name='locations_landing'),
    url(r'^(?P<slug>\w+)/$', 'detail', name='locations_detail'),
)
