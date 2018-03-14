"""
Django settings for stockingdjango project.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
  "default": 
  {
   "ENGINE": "django.db.backends.postgresql_psycopg2", #one of those should work
   'ENGINE': 'django.db.backends.postgresql',   #one of those should work
   "NAME": 'PostgreSQL 10',
   'USER': 'postgres',
   'PASSWORD': 'pass',
   "HOST": "localhost", 
   "PORT": "5432",
   'OPTIONS': {
            'autocommit': True,
        },
  }
}

DEBUG = True
TEMPLATES = [
{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'stocking/templates'),'templates'],
    'APP_DIRS': True,
    'OPTIONS': {
        'debug': DEBUG,
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
    },
}
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '+we06q!vu7)e-01^o@_4$*2$q$zh2u9=k08yfzhp0@^iws!gto'

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'stocking',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'stockingdjango.urls'

WSGI_APPLICATION = 'stockingdjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
#import dj_database_url
#DATABASES['default'] =  dj_database_url.config()

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

# Parse database configuration from $DATABASE_URL
import dj_database_url
DATABASES['default'] =  dj_database_url.config()
#DATABASES['default'] = dj_database_url.config(default='postgres://postgres:pass@localhost/test')

#DATABASES['default'] = dj_database_url.config(default='postgres://bsmdtcly:s7nnVJnb16OBIyc2aFbE2ecHcb-nNKMs@hanno-01.db.elephantsql.com:5432/bsmdtcly')
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

LOGIN_REDIRECT_URL = '/stocks/home'
LOGIN_URL='/auth/login/'
