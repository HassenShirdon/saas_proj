from datetime import timedelta
from pathlib import Path
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = os.getenv('SECRET_KEY')
if not SECRET_KEY:
    raise ValueError("SECRET_KEY must be set in .env file")

DEBUG = os.getenv('DEBUG', 'False').lower() == 'true'  # Convert string to boolean

ALLOWED_HOSTS = ['*']  # Fixed typo

# For SaaS, allow tenant domains dynamically
TENANT_SUBFOLDER_PREFIX = None  # Set if using subfolder-based tenants


# Shared and tenant-specific apps
SHARED_APPS = [
    'django_tenants',
    # 'django.contrib.admin',  # Added for public schema admin
    # 'django.contrib.auth',  # Added for authentication
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework_simplejwt',
    'core',
    
]

TENANT_APPS = [
    'django.contrib.contenttypes',
    'rest_framework',
    'django.contrib.admin',
    'django.contrib.auth',
    'rest_framework_simplejwt',
    'django.contrib.sessions',
    'django.contrib.messages',
    'inventory',
    'finance',
    'hrm',
    'users',
]

# Custom user roles for tenants
TENANT_USER_ROLES = [
    ('finance_manager', 'Finance Manager'),
    ('operation_manager', 'Operation Manager'),
    ('administrator', 'Administrator'),
    ('human_resource_manager', 'Human Resource Manager'),
]

INSTALLED_APPS = list(SHARED_APPS) + [app for app in TENANT_APPS if app not in SHARED_APPS]

# Tenant configuration
TENANT_MODEL = "core.Client"  # Ensure core.Client exists
TENANT_DOMAIN_MODEL = "core.Domain"  # Ensure core.Domain exists
PUBLIC_SCHEMA_NAME = 'public'  # Explicitly define public schema
#PUBLIC_SCHEMA_URLCONF = 'proj_saas.urls_public'  # Optional: for public schema
SHOW_PUBLIC_IF_NO_TENANT_FOUND = True  # Fallback to public schema

# Middleware
MIDDLEWARE = [
    'django_tenants.middleware.main.TenantMainMiddleware',  # Must be first
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# URL configuration
ROOT_URLCONF = 'proj_saas.urls'

# REST Framework configuration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
        'rest_framework.authentication.SessionAuthentication', 
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
}

# CORS configuration
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
    'http://localhost:8000',
    'http://jeeh.localhost:8000',
    'http://jeeh.localhost:5173',
    'http://demo.localhost:5173',
    'http://demo.localhost:8000',

    # Add tenant-specific domains dynamically in production
]
CORS_ALLOW_CREDENTIALS = True  # Allow credentials for JWT

# JWT configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=7),  # Added for sliding refresh
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'UPDATE_LAST_LOGIN': True,  # Track last login
    'ALGORITHM': 'HS256',
    'SIGNING_KEY': os.getenv('SECRET_KEY'),
    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

# Database configuration
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': os.getenv('DATABASE_NAME'),
        'USER': os.getenv('DATABASE_USER'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD'),
        'HOST': os.getenv('DATABASE_HOST', 'localhost'),
        'PORT': os.getenv('DATABASE_PORT', '5432'),
    }
}

# Database routers
DATABASE_ROUTERS = ['django_tenants.routers.TenantSyncRouter']

# Template configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Added for custom templates
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

# WSGI application
WSGI_APPLICATION = 'proj_saas.wsgi.application'

# Authentication
AUTH_USER_MODEL = 'users.CustomUser'

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static and media files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For collectstatic
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'

# Logging configuration
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django_tenants': {
            'handlers': ['console'],
            'level': 'DEBUG' if DEBUG else 'INFO',
        },
    },
}

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


