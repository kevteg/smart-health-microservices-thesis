"""
Django settings for services project.
Thesis project
"""
import os
from configurations import Configuration

class Base(Configuration):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    SECRET_KEY = 'i)7ek7t^%!8-gd^d(9f)=ii1!x)w$gvpc$8st$!g9+tb#0h-fc'
    DEBUG = os.environ.get('DEBUG', True)
    ALLOWED_HOSTS = ['*']
    ROOT_URLCONF = 'urls'
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = os.path.join(BASE_DIR, 'staticfiles/')
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]



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

    WSGI_APPLICATION = 'wsgi.application'
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

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
    AUTH_USER_MODEL = 'auth.User'


class Gateway(Base):
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Gateway.apps.GatewayConfig',
    ]
    MED_RECORDS_URL = os.environ.get('MED_RECORDS_URL', 'http://192.168.0.90:4444') 
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'NAME': os.environ.get('DB_NAME'),
            'HOST': os.environ.get('DB_NAME'),
        }
    }


class Medrecords(Base):
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Medrecords.apps.MedRecordsConfig',
        'graphene_django',
    ]
    GRAPHENE = {
        'SCHEMA': 'Medrecords.schema.schema'
    }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'NAME': os.environ.get('DB_NAME'),
            'HOST': os.environ.get('DB_NAME'),
        }
    }


class Mhealth(Base):
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Mhealth.apps.MhealthConfig',
        'graphene_django',
    ]
    GRAPHENE = {
        'SCHEMA': 'Mhealth.schema.schema'
    }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'NAME': os.environ.get('DB_NAME'),
            'HOST': os.environ.get('DB_NAME'),
        }
    }


class Statistics(Base):
    # Application definition

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'Statistics.apps.StatisticsConfig',
    ]
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'USER': os.environ.get('POSTGRES_USER'),
            'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
            'NAME': os.environ.get('DB_NAME'),
            'HOST': os.environ.get('DB_NAME'),
        }
    }
