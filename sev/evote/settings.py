
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, "sevapp/static")



SECRET_KEY = 'qg5tg(_tq5g0s1p_hr&u(9)2%dw_v(!67j%to+t*6sk4z+st3s'


DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']



INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'phone_login',                      #changed    
    #'rest_framework',                   #changed
    #'rest_framework.authtoken',         #changed
    'sevapp',
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


ROOT_URLCONF = 'evote.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR],
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

WSGI_APPLICATION = 'evote.wsgi.application'
#Added rest_framework here
#REST_FRAMEWORK = {
#    'DEFAULT_AUTHENTICATION_CLASSES': (
 #       'rest_framework.authentication.BasicAuthentication',
  #      'rest_framework.authentication.TokenAuthentication',
   # )
#}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}



PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
]

#added authentication_backends here
#AUTHENTICATION_BACKENDS = [
 #   'phone_login.backends.phone_backend.PhoneBackend',
  #  'django.contrib.auth.backends.ModelBackend'
#]



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

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [
    STATIC_DIR, 
]
LOGIN_URL = '/login/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'varthi@1507'
EMAIL_HOST_USER = 'rvsvarthini@gmail.com'
EMAIL_USE_SSL = False
EMAIL_USE_TLS = True
EMAIL_PORT = 587

#added these 4 lines for otp 
#SENDSMS_BACKEND = 'myapp.mysmsbackend.SmsBackend' #(defaults to 'sendsms.backends.console.SmsBackend')
#SENDSMS_FROM_NUMBER = "+918056688630"
#SENDSMS_ACCOUNT_SID = 'ACXXXXXXXXXXXXXX'
#SENDSMS_AUTH_TOKEN = 'xxxxxxxx'