import os

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SERVER_EMAIL = 'errors@globecard.ca'
DEFAULT_FROM_EMAIL = 'no-reply@globecard.ca'

ADMINS = (
    ('Taylan Pince', 'taylanpince@gmail.com'),
)

MANAGERS = ADMINS

TIME_ZONE = 'Canada/Eastern'

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'en'

SITE_ID = 1

MEDIA_ROOT = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'media/')
MEDIA_URL = '/media/'

SECRET_KEY = 'w5($l55v%2wprhhvoe2icc(@7qkz9%@xd1tl9dy1r+v(6#xlq#'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'globecard.urls'

TEMPLATE_DIRS = (
    os.path.join(os.path.realpath(os.path.dirname(__file__)), 'templates/'),
)

MARKITUP_FILTER = ('markdown.markdown', {})
MARKITUP_SET = 'markitup/sets/markdown'
MARKITUP_AUTO_PREVIEW = True

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.markup',

    'django_extensions',
    'markitup',
    'sorl.thumbnail',
    'south',

    'careers',
    'events',
    'locations',
    'news',
    'offices',
    'pages',
    'publisher',
)

try:
    from settings_local import *
except:
    pass

ADMIN_MEDIA_PREFIX = MEDIA_URL + 'admin/'
