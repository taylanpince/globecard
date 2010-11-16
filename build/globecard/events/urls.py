from django.conf.urls.defaults import *


urlpatterns = patterns('events.views',
    url(r'^$', 'list', name='events_list'),
)
