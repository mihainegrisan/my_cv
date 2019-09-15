"""
Django settings for cv project.

Generated by 'django-admin startproject' using Django 2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qu$6!t+(zl_0ab0a_dl5ag6x7+z@g#7+xof#u^e(n^dnis_nx2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['mysite.com', 'localhost', '127.0.0.1', '.pythonanywhere.com']


# Application definition

INSTALLED_APPS = [
    'account',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'pages',
    'web_design',
    'taggit',
    'blog.apps.BlogConfig',
    'social_django',

    # E-commerce
    'shop',
    'cart',
    'orders',
    # 'payment',

    'widget_tweaks',
    'admin_honeypot',
    # 'django_celery_results', install before uncommenting
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


    'social_django.middleware.SocialAuthExceptionMiddleware', # <--
]

ROOT_URLCONF = 'cv.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',  # <--
                'social_django.context_processors.login_redirect', # <--
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'cv.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Bucharest'
USE_I18N = True
USE_L10N = True
USE_TZ = True



STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'static_cdn') # content delivery network
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media_cdn')


# EMAIL CONFIGURATION
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'mihainegrisan.cv@gmail.com'
EMAIL_HOST_PASSWORD = '1qaz2wsx3edc!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Celery - Redis
# CELERY_BROKER_URL = 'redis://localhost'
# CELERY_RESULT_BACKEND = 'redis://localhost:6379'
# CELERY_ACCEPT_CONTENT = ['application/json']
# CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TASK_SERIALIZER = 'json'

# add to requirements.txt django-celery-results==1.1.2
# CELERY_RESULT_BACKEND = 'django-db'
# CELERY_CACHE_BACKEND = 'django-cache'
# CELERY_TASK_ALWAYS_EAGER = ?



LOGIN_REDIRECT_URL = 'account:dashboard'
LOGIN_URL = 'account:login'
LOGOUT_URL = 'account:logout'

AUTHENTICATION_BACKENDS = (
    #'social_core.backends.github.GithubOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',

    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',

)

# SECURE_SSL_REDIRECT = True

if DEBUG == True:
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

    SOCIAL_AUTH_FACEBOOK_KEY = '500657657173593' # Facebook App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = '69df7169ee117bd21cfc7ea40d8f51fd' # Facebook App Secret
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1053881313048-ki6ajljemcns6ou60ee1skj4a9bbg9lm.apps.googleusercontent.com' # Google Consumer Key
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '8jDm82jSjrOsNln3QJGwq9ly' # Google Consumer Secret
else:
    SOCIAL_AUTH_FACEBOOK_KEY = '445334359632844' # Facebook App ID
    SOCIAL_AUTH_FACEBOOK_SECRET = '77807ab18529c7ee024839d740dffb6e' # Facebook App Secret
    SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '585939395621-tgbl6hierobpkc6h3pe1uj04ok6ip2l5.apps.googleusercontent.com' # Google Consumer Key
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '81xazK6Sqj0SXzKJl0Bq3ANc' # Google Consumer Secret


# This is the key that we are going to use to store the cart in the user session.
# Since Django sessions are managed per-visitor, we can use the same cart session key for all sessions.
CART_SESSION_ID = 'cart'



# Braintree settings
# BRAINTREE_MERCHANT_ID = 'ccvs8jm6wwb4dkxx' # Merchant ID
# BRAINTREE_PUBLIC_KEY = 'w2zz9zwvfbd4xxgc' # Public Key
# BRAINTREE_PRIVATE_KEY = '1d7e3e6fab33f6b09757639f4b004fce' # Private key
#
# from braintree import Configuration, Environment
#
# Configuration.configure(
#     # Environment.Production,
#     Environment.Sandbox,
#     BRAINTREE_MERCHANT_ID,
#     BRAINTREE_PUBLIC_KEY,
#     BRAINTREE_PRIVATE_KEY
# )
