from pathlib import Path

import environ


env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = env('SECRET_KEY', default='YOUR_SECRET_KEY')

DEBUG = env.bool('DEBUG', default=False)

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS', default=['*'])

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'leaflet',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.vk',
    'places',
    'users',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': env('ENGINE_DB', default='django.contrib.gis.db.backends.postgis'),
        'NAME': env('POSTGRES_DB', default='postgres'),
        'USER': env('POSTGRES_USER', default='postgres'),
        'PASSWORD': env('POSTGRES_PASSWORD', default='postgres'),
        'HOST': env('POSTGRES_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='5432'),
    }
}

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

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = ('allauth.account.auth_backends.AuthenticationBackend',)

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_URL = 'places:index'
LOGIN_REDIRECT_URL = 'places:home'
LOGOUT_REDIRECT_URL = 'places:home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'places:home'
ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_PROVIDERS = {
    'github': {
        'SCOPE': ['email'],
        'APP': {
            'client_id': env('GITHUB_CLIENT_ID'),
            'secret': env('GITHUB_SECRET'),
        }
    },
    'vk': {
        'SCOPE': ['email'],
        'APP': {
            'client_id': env('VK_CLIENT_ID'),
            'secret': env('VK_SECRET'),
        }
    },
    'mailru': {
        'SCOPE': ['email'],
        'APP': {
            'client_id': env('MAILRU_CLIENT_ID'),
            'secret': env('MAILRU_SECRET'),
        }
    }
}

LEAFLET_CONFIG = {
    'DEFAULT_CENTER': (56.002778, 92.854167),
    'DEFAULT_ZOOM': 10,
    'MAX_ZOOM': 18,
    'MIN_ZOOM': 3,
    'SCALE': 'both',
    'ATTRIBUTION_PREFIX': 'Leaflet',
}
