import os
from pathlib import Path
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = os.environ.get("SECRET_KEY")
SECRET_KEY =  'django-insecure-n*&w+5o-6+6$gy8%%3##q!%)#g+kfcddg@5mu81tym_s-5ymoz'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#ALLOWED_HOSTS =("ALLOWED_HOST").split(" ")
ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    #"admin_interface",
    #"colorfield",
    #'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'polls'
    #'crispy_forms'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'basseac.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'basseac.wsgi.application'

CSRF_TRUSTED_ORIGINS = [
    #'https://www.basse.gm',
    #'https://basse.gm',

    'https://www.bac-website-production.up.railway.app',
    'https://bac-website-production.up.railway.app',

]
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

#DATABASES = {
    #'default': {
        #'ENGINE':'django.db.backends.postgresql',
        #'NAME':'railway',
        #'USER':'postgres',
        #'PASSWORD':'UNjwtBdkivCFgbtvWxkDIdCFqxgkemnG',
        #'HOST':'viaduct.proxy.rlwy.net',
        #'PORT':'21414',
    #}
#}

#DATABASES = {
    #'default': {
       # 'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
    #}
#}


DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.postgresql',
        'NAME':'railway',
        'USER':'postgres',
        'PASSWORD':'BDlGkUjGxyOAjkXvYOcNxmHcZxRFlCRi',
        'HOST':'viaduct.proxy.rlwy.net',
        'PORT':'21042',
    }
}



    


#DATABASES['default'] = dj_database_url.parse('postgres://admin:rLWudigC266aduRxCw9qIiv4qy9I2NcM@dpg-cnvn6l6ct0pc73dnnfug-a.oregon-postgres.render.com/basse')

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static'),

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

from django.contrib.messages import constants as messages
MESSAGE_TAGS ={
    messages.ERROR:'danger'
}


MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')
