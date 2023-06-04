"""
Django settings for project project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import environ
from pathlib import Path
from django.utils.translation import gettext_lazy as _

from celery.schedules import crontab
from django.urls import reverse_lazy

# import sentry_sdk
# from sentry_sdk.integrations.django import DjangoIntegration

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    debug=True
)

environ.Env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env.str('SECRET_KEY', default='SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool('DEBUG', default=True)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=[])
ENABLE_SILK = env.bool('ENABLE_SILK', default=False)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'debug_toolbar',
    # external
    'widget_tweaks',
    'django_celery_results',
    'django_celery_beat',
    'django_extensions',
    'rosetta',

    # internal
    'products',
    'orders',
    'feedbacks',
    'accounts',
    'main',
    'tracking',
    'currencies',
    'favourites',
]

if ENABLE_SILK:
    INSTALLED_APPS.append('silk')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'project.middlewares.TrackingMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

if ENABLE_SILK:
    MIDDLEWARE.append('silk.middleware.SilkyMiddleware')

if DEBUG:
    MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = [
    '127.0.0.1',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'project.context_processors.slug_categories',
                'project.context_processors.products_in_cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        "OPTIONS": {
            # ...
            "timeout": 20,
            # ...
        }
    }

}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # noqa
    },
]

LOGIN_REDIRECT_URL = reverse_lazy("main")
LOGOUT_REDIRECT_URL = LOGIN_REDIRECT_URL
AUTH_USER_MODEL = 'accounts.User'

AUTHENTICATION_BACKENDS = [
    "accounts.auth_backends.EmailOrPhoneModelBackend"
]

# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = [
    ('uk', _('Ukrainian')),
    ('en', _('English')),
]

LOCALE_PATHS = [
    BASE_DIR / 'locale'
]

TIME_ZONE = 'Europe/Kiev'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = 'static_files'
STATICFILES_DIRS = ['assets']
MEDIA_URL = 'media/'
MEDIA_ROOT = 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CELERY_BROKER_URL = env('CELERY_BROKER_URL', default='CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = 'django-db'

CELERY_BEAT_SCHEDULE = {
    'Get currencies': {
        'task': 'currencies.tasks.get_currencies_task',
        'schedule': crontab(hour='19', minute='0'),
    },
    'Set currencies': {
        'task': 'currencies.tasks.set_currencies_task',
        'schedule': crontab(hour='19', minute='2'),
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.redis.RedisCache",
#         "LOCATION": "redis://127.0.0.1:6379",
#         "TIMEOUT": 3600,
#     }
# }

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
        "TIMEOUT": 3600,
    }
}

APPEND_SLASH = True

# ADMINS = env.list('ADMINS', default='ADMINS')
ADMINS = (('Admin', 'lobach.igor.olegovich@gmail.com'),)
# out to console
# EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = env.str('EMAIL_HOST', default='EMAIL_HOST')
EMAIL_PORT = env.str('EMAIL_PORT', default='EMAIL_PORT')
EMAIL_HOST_USER = env.str('EMAIL_HOST_USER', default='EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env.str('EMAIL_HOST_PASSWORD',
                              default='EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env.bool('EMAIL_USE_TLS', default=True)

SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

EMAIL_SUBJECT_PREFIX = 'Shop - '

# tool for error's monitoring

# sentry_sdk.init(
#     dsn="https://dedc08f902a3406f9982023fe43beb1e@o4505081808"
#         "486400.ingest.sentry.io/4505081809993728",
#     integrations=[
#         DjangoIntegration(),
#     ],
#     # Set traces_sample_rate to 1.0 to capture 100%
#     # of transactions for performance monitoring.
#     # We recommend adjusting this value in production.
#     traces_sample_rate=0.5,
#
#     # If you wish to associate users to errors (assuming you are using
#     # django.contrib.auth) you may enable sending PII data.
#     send_default_pii=True
# )

try:
    from project.settings_local import *  # noqa
except ImportError:
    ...
