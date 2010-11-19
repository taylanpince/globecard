from django.conf.urls.defaults import *
from django.contrib import admin


admin.autodiscover()


urlpatterns = patterns('',
    # Admin
    (r'^admin/', include(admin.site.urls)),

    # Events
    (r'^events/', include("events.urls")),

    # Locations
    (r'^locations/', include("locations.urls")),

    # Offices
    (r'^offices/', include("offices.urls")),

    # News
    (r'^news/', include("news.urls")),

    # Careers
    (r'^careers/', include("careers.urls")),
)
