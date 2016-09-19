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
