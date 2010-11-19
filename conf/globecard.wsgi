import os
import sys
import site

site.addsitedir('/home/globecardteam/sites/globecard/lib/python2.4/site-packages')

sys.path.append("/home/globecardteam/sites/globecard/src/globecard/build")
sys.path.append("/home/globecardteam/sites/globecard/src/globecard/build/globecard")

os.environ["DJANGO_SETTINGS_MODULE"] = "globecard.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
