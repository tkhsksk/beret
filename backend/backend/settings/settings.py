from .settings_common import *

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'beret',
        'USER': 'dev',
        'PASSWORD': 'NMHLJMTS2LWHU28MFBVG',
        'HOST': 'localhost',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

CSRF_TRUSTED_ORIGINS = [ "https://django.ksk318.me" ]

# TailwindCSS settings
TAILWIND_APP_NAME = 'tailwind_theme'
INTERNAL_IPS = [
    'localhost',
]
