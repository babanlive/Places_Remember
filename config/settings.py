from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-dvs-&o*b1dru)925uo62l74q=2(w!)rnlz5-33-d&=(416nheo'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.mailru',
    'allauth.socialaccount.providers.vk',
    # apps
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
    # Add the account middleware:
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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# social_app/settings.py

AUTHENTICATION_BACKENDS = ('allauth.account.auth_backends.AuthenticationBackend',)

SITE_ID = 1
ACCOUNT_EMAIL_VERIFICATION = 'none'
LOGIN_REDIRECT_URL = 'places:home'
LOGOUT_REDIRECT_URL = 'places:home'
ACCOUNT_LOGOUT_REDIRECT_URL = 'places:home'
ACCOUNT_LOGOUT_ON_GET = True

SOCIALACCOUNT_FORMS = {
    'signup': 'users.forms.CustomSignupForm',
    'login': 'users.forms.CustomLoginForm',
}


SOCIALACCOUNT_PROVIDERS = {
    "github": {
        "SCOPE": [
            "email",
        ],
        "APP": {
            "client_id": "Ov23liZMWapJJlmue4Pu",
            "secret": "9fde05c68d364058147c913fda1de35d043818a9",
        }
    },
    "vk": {
        "SCOPE": [
            "email",
        ],
        "APP": {
            "client_id": "51931051",
            "secret": "h3uPJJ3EsX6MwSgJgWrx",
        }
    },
    "mailru": {
        "SCOPE": [
            "email",
        ],
        "APP": {
            "client_id": "172062da00f7438784ea90b2e0ca631e",
            "secret": "0e0ff31aad5142dea52ad94948cbe2a0",
        }
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
