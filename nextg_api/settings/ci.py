from .base import *

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

INSTALLED_APPS.append('django_nose')

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=%s' % (','.join(MANUALLY_BUILT_APPS)),
    '-cover-inclusive',
]

