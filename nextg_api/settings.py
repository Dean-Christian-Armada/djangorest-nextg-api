"""
Django settings for nextg_api project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')@kqdcf)0l@l37m@r(_ng3-loe%5j@0g!-h@uju0qek@%m&r7l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MANUALLY_BUILT_APPS = [
    'core',
    'core.conversations',
    'core.reports',
    'core.groups',
    'core.accounts',
    'system_admin',
    'assessor',
    'workplace_supervisor',
    'students',
]
INSTALLED_APPS += MANUALLY_BUILT_APPS

THIRD_PARTY_APPS = [
    'corsheaders',
    'rest_framework', # Restful API library for Django
    'oauth2_provider', # Oauth2 library especially made for django with django rest framework integration
    'rest_framework_docs', # Library for creating API Documentation
    'markdown',
]
INSTALLED_APPS += THIRD_PARTY_APPS

MIDDLEWARE = [
    # https://github.com/evonove/django-oauth-toolkit/pull/300/files
    # 'oauth2_provider.middleware.CorsMiddleware', # To let the allowed_uris be the CORSHeader whitelist
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nextg_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nextg_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "NextG",
        "USER": "nextg",
        "PASSWORD": "Qvdj9WVBe9IpGGzoprukHpKfWnm25MwR",
        "HOST": "nextgrds-development.cufynjh7w7r3.ap-southeast-2.rds.amazonaws.com",
        "PORT": "5432"
    }
}

if os.environ.get('BITBUCKETPIPELINES', '0') == '1':
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "NextG",
            "USER": "root",
            "PASSWORD": "pass1234",
            "HOST": "127.0.0.1",
            "PORT": "5432"
        }
    }
# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = False # Set to False to import optimizations

USE_L10N = True

USE_TZ = True

# Source: fideloper.com/api-etag-conditional-get
# Use "If-None-Match" header with Etag
# Work with client on this carefully
USE_ETAGS = True # For caching mechanism

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

# START Django Rest Framework settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'oauth2_provider.ext.rest_framework.OAuth2Authentication',
    ),
    # Disables the Admin UI of the Django Rest Framework
    # Source: http://stackoverflow.com/questions/11898065/how-to-disable-admin-style-browsable-interface-of-django-rest-framework
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    )
}
# END Django Rest Framework settings

CORS_ORIGIN_ALLOW_ALL = True

OAUTH2_PROVIDER = {
    "ACCESS_TOKEN_EXPIRE_SECONDS": 7776000 # 3 months
}