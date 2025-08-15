from pathlib import Path
import mongoengine
import os
from dotenv import load_dotenv
import ssl
import certifi

# Load environment variables from .env file
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / '.env')

def connect_mongodb_atlas():
    """
    Custom function to connect to MongoDB Atlas with multiple fallback strategies
    for handling SSL/TLS handshake issues.
    """
    connection_string = os.getenv('MONGODB_ATLAS_URI', 
        'mongodb+srv://hieu:hieu@cluster0.yrpxm.mongodb.net/ReHearten_db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
    )
    db_name = os.getenv('MONGODB_ATLAS_DB', 'ReHearten_db')
    
    # Strategy 1: Try with full SSL verification
    try:
        print("🔒 Attempting connection with full SSL verification...")
        mongoengine.connect(
            db=db_name,
            host=connection_string,
            alias='default',
            tls=True,
            tlsAllowInvalidCertificates=False,
            tlsAllowInvalidHostnames=False,
            tlsCAFile=certifi.where(),
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000,
            maxPoolSize=10,
            minPoolSize=1,
            maxIdleTimeMS=30000,
            retryWrites=True,
            retryReads=True,
            authMechanism='SCRAM-SHA-1'
        )
        print("✅ Connected with full SSL verification!")
        return True
    except Exception as e1:
        print(f"⚠️ Full SSL verification failed: {e1}")
    
    # Strategy 2: Try with relaxed SSL settings
    try:
        print("🔓 Attempting connection with relaxed SSL settings...")
        mongoengine.connect(
            db=db_name,
            host=connection_string,
            alias='default',
            tls=True,
            tlsAllowInvalidCertificates=True,
            tlsAllowInvalidHostnames=True,
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000,
            maxPoolSize=10,
            minPoolSize=1,
            maxIdleTimeMS=30000,
            retryWrites=True,
            retryReads=True,
            authMechanism='SCRAM-SHA-1'
        )
        print("✅ Connected with relaxed SSL settings!")
        return True
    except Exception as e2:
        print(f"⚠️ Relaxed SSL settings failed: {e2}")
    
    # Strategy 3: Try with minimal SSL configuration
    try:
        print("🔧 Attempting connection with minimal SSL configuration...")
        mongoengine.connect(
            db=db_name,
            host=connection_string,
            alias='default',
            serverSelectionTimeoutMS=30000,
            connectTimeoutMS=30000,
            socketTimeoutMS=30000,
            maxPoolSize=10,
            minPoolSize=1,
            maxIdleTimeMS=30000,
            retryWrites=True,
            retryReads=True
        )
        print("✅ Connected with minimal SSL configuration!")
        return True
    except Exception as e3:
        print(f"❌ All connection strategies failed!")
        print(f"Error 1: {e1}")
        print(f"Error 2: {e2}")
        print(f"Error 3: {e3}")
        return False


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&(2xt*_5eoht1+00eudkbni74$r5haman_h0)yd!_9x&*=tfgf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'accounts',
    'social_django', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'accounts.process_login_gg.SyncCustomSessionMiddleware',  # Đồng bộ session custom sau Google login
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'REHEARTEN.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'REHEARTEN.wsgi.application'




# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# Use dummy database since we're using only MongoDB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Disable Django's database migrations since we're using MongoDB
MIGRATION_MODULES = {
    'accounts': None,
    # 'admin': None,
    # 'auth': None,
    # 'contenttypes': None,
    # 'sessions': None,
    # 'messages': None,
}

# Authentication Backends
AUTHENTICATION_BACKENDS = [
    'accounts.backends.MongoUserBackend',
    'social_core.backends.google.GoogleOAuth2',  # Google OAuth2 backend
    'django.contrib.auth.backends.ModelBackend',  # Thêm dòng này!
]

# MongoDB Configuration - Support both Local and Atlas

# MongoDB Atlas Configuration
MONGODB_ATLAS_SETTINGS = {
    'CONNECTION_STRING': os.getenv('MONGODB_ATLAS_URI', 
        'mongodb+srv://hieu:hieu@cluster0.yrpxm.mongodb.net/ReHearten_db?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE'
    ),
    'DB_NAME': os.getenv('MONGODB_ATLAS_DB', 'ReHearten_db'),
}

# Connect to MongoDB Atlas only
print("🌐 Connecting to MongoDB Atlas...")
if connect_mongodb_atlas():
    MONGODB_INFO = {
        'TYPE': 'MongoDB Atlas (Cloud)',
        'DATABASE': MONGODB_ATLAS_SETTINGS['DB_NAME'],
        'CONNECTION': 'Atlas Cloud Cluster - ReHearten'
    }
    print("✅ MongoDB Atlas connection established successfully!")
else:
    print("❌ MongoDB Atlas Connection Error: All connection strategies failed!")
    print("🔥 Application cannot start without MongoDB Atlas connection!")
    raise Exception("MongoDB Atlas connection failed: All connection strategies failed!")

# Session Configuration - Use MongoDB sessions instead of Django's database sessions
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'vi-VN'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Social Auth Google OAuth2 settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('GOOGLE_OAUTH2_CLIENT_ID', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('GOOGLE_OAUTH2_CLIENT_SECRET', '')
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['email', 'profile']
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard/'
LOGOUT_REDIRECT_URL = '/'



SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'accounts.process_login_gg.process_login_gg',  # pipeline Google + session custom
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {process:d} {thread:d} {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
        },
        'file': {  # Add the missing file handler
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': BASE_DIR / 'logs' / 'django.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'accounts': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
        

    },
}



# Add these lines after the MongoDB configuration section (around line 140)

