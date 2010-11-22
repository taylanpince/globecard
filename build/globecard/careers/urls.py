from django.conf.urls.defaults import *


urlpatterns = patterns('careers.views',
    url(r'^positions/$', 'list', name='careers_list'),
    url(r'^apply/$', 'apply', name='careers_apply'),
    url(r'^apply/thank-you/$', 'apply_done', name='careers_apply_done'),
)
