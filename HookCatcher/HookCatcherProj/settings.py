"""
Django settings for HookCatcherProj project.

Generated by 'django-admin startproject' using Django 1.10.3.

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
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY') or 'qwnj&01%5_q$j+&v**2o9mafh+zt9^y^ntgkr#wp+a125ky(ta'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'HookCatcher.apps.HookcatcherConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_rq',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'HookCatcherProj.urls'

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

WSGI_APPLICATION = 'HookCatcherProj.wsgi.application'


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

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')

MEDIA_URL = '/media/'


# --- GET ALL THE OTHER ENV VARIABLES ---
# GIT_REPO = os.getenv('GIT_REPO')    # the Github Repository you are attempting to link to

# GIT_OAUTH = os.getenv('GIT_OAUTH')  # your Github Access Token

# # the name of the directory in the Git Repository that stores the state representation JSON files.
# STATES_FOLDER = os.getenv('STATES_FOLDER')

# # Local file path of the directory being pointed to used to switch branches (depreicated)
# WORKING_DIR = os.getenv('WORKING_DIR') or ''

# # File to set what specific screenshot settings you want
# SCREENSHOT_CONFIG = os.getenv('SCREENSHOT_CONFIG')

# # browser stack api username
# BROWSERSTACK_USERNAME = os.getenv('BROWSERSTACK_USERNAME') or ''

# # browser stack api authentication *need subscription*
# BROWSERSTACK_OAUTH = os.getenv('BROWSERSTACK_OAUTH') or ''

# try to get the env variable for Postgres port
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
if not POSTGRES_PORT:
    POSTGRES_PORT = 5432


# Load user specific settings saved in a separate file
try:
    execfile(os.path.join(BASE_DIR, "user_settings.py"), globals(), locals())
except NameError:
    with open(os.path.join(BASE_DIR, "user_settings.py")) as f:
        code = compile(f.read(), os.path.join(BASE_DIR, "user_settings.py"), 'exec')
        exec(code, globals(), locals())
except IOError:
    pass

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'garnish_db',
        'USER': 'garnish_user',
        'PASSWORD': 'garnish',
        'HOST': '127.0.0.1',
        'PORT': POSTGRES_PORT,
    }
}

# try to get the env variable for Redis port
REDIS_PORT = os.getenv('REDIS_PORT')
if not REDIS_PORT:
    REDIS_PORT = 6379

RQ_QUEUES = {
    'default': {
        'HOST': 'localhost',
        'PORT': REDIS_PORT,
        'DB': 0,
        'PASSWORD': '',
        'DEFAULT_TIMEOUT': 360,
    },
}
