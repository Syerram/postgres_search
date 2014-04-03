"""
Django settings for postgres_search project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os
from django.core.exceptions import ImproperlyConfigured

DEBUG = True
TEMPLATE_DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = 'qed*!j!zwlmqf%z^d!fy%hedtnjqr!-fjs24dc1zq_m5r40hd('

ALLOWED_HOSTS = []
INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        # internal
        'course',
        'student',
        'search',

        # party
        'south',
        'kombu.transport.django'
)

MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'postgres_search.urls'

WSGI_APPLICATION = 'postgres_search.wsgi.application'

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
        }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'web/static'),)
STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

TEMPLATE_LOADERS = (
        ('django.template.loaders.cached.Loader',
            (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader')
            ),
        )

TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'web/templates'),
        )

TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.debug',
        'django.core.context_processors.i18n',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.core.context_processors.tz',
        'django.contrib.messages.context_processors.messages',
        'django.core.context_processors.request'
)

def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return os.environ[setting]
    except KeyError:
        error_msg = 'Set the %s env variable' % setting
        raise ImproperlyConfigured(error_msg)
