# backend/recommendation_engine/settings.py
import os
from pathlib import Path
import dj_database_url # Add this import

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# We will set this via environment variable later
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'django-insecure-your-default-development-key') # Default for dev

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True' # Default True for dev

ALLOWED_HOSTS = ['localhost', '127.0.0.1'] # Add Heroku app URL later
# For deployment, get host from env var
HEROKU_APP_NAME = os.environ.get('HEROKU_APP_NAME')
if HEROKU_APP_NAME:
    ALLOWED_HOSTS.append(f"{HEROKU_APP_NAME}.herokuapp.com")


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # Add Whitenoise
    'django.contrib.staticfiles',
    # Third-party apps
    'rest_framework',
    'corsheaders',
    # Your apps
    'recommendations',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Add Whitenoise middleware AFTER SecurityMiddleware
    'corsheaders.middleware.CorsMiddleware', # Add CORS middleware (Important!)
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recommendation_engine.urls'

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

WSGI_APPLICATION = 'recommendation_engine.wsgi.application'

# Database
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
# Use dj-database-url to parse the DATABASE_URL environment variable
DATABASES = {
    'default': dj_database_url.config(
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', # Default to SQLite for local dev
        conn_max_age=600 # Optional: connection pooling
    )
}


# Password validation
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    # ... (keep defaults)
]

# Internationalization
# https://docs.djangoproject.com/en/stable/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/stable/howto/static-files/
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles' # Directory where collectstatic will gather static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage' # Whitenoise storage

# Default primary key field type
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Django REST Framework settings (optional, can add later if needed)
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # Add BrowsableAPIRenderer only if DEBUG is True
        # 'rest_framework.renderers.BrowsableAPIRenderer',
    ],
     # Add authentication/permission classes if needed later
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [],
}
# Add Browsable API only in development
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')


# CORS Settings (VERY IMPORTANT for Frontend <-> Backend communication)
# Allow requests from your Vue app's domain during development and production
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",  # Default Vue dev server port
    "http://127.0.0.1:8080",
    # Add Netlify/Vercel frontend URL later
]
# If using credentials (like cookies or auth headers), set:
# CORS_ALLOW_CREDENTIALS = True

# Optional: Allow specific headers or methods if needed
# CORS_ALLOW_METHODS = [...]
# CORS_ALLOW_HEADERS = [...]

# Set CORS_ALLOWED_ORIGIN_REGEXES if you have dynamic frontend previews on Netlify/Vercel
# Example for Netlify deploy previews:
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://\w+--your-netlify-app-name\.netlify\.app$",
# ]
# Example for Vercel previews:
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://your-vercel-project-name-.*\.vercel\.app$",
# ]

# Environment variable for frontend URL (better approach)
FRONTEND_URL = os.environ.get('FRONTEND_URL')
if FRONTEND_URL:
    CORS_ALLOWED_ORIGINS.append(FRONTEND_URL)