# backend/recommendation_engine/settings.py

import os
from pathlib import Path
import dj_database_url  # To parse DATABASE_URL environment variable

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# --- Core Settings ---

# SECURITY WARNING: keep the secret key used in production secret!
# Read from environment variable in production. Provide a default for local dev.
# Generate a real one for production using:
# python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
SECRET_KEY = os.environ.get(
    'DJANGO_SECRET_KEY',
    'django-insecure-=your_temporary_development_key_!@#$%^' # <-- CHANGE THIS for local dev if you want
)

# SECURITY WARNING: don't run with debug turned on in production!
# Read from environment variable. Defaults to True for local dev.
# Set DJANGO_DEBUG=False in your production environment (e.g., PythonAnywhere WSGI or Heroku Config Vars)
DEBUG = os.environ.get('DJANGO_DEBUG', 'True') == 'True'

# Define allowed hosts. Start with local hosts.
# Add your production domain(s) here or read from an environment variable.
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Add PythonAnywhere domain if set via environment variable
# (Set PYTHONANYWHERE_DOMAIN=your-username.pythonanywhere.com in your WSGI file or env vars)
pythonanywhere_domain = os.environ.get('PYTHONANYWHERE_DOMAIN')
if pythonanywhere_domain:
    ALLOWED_HOSTS.append(pythonanywhere_domain)

# Add Heroku domain if set via environment variable (example)
# (Set HEROKU_APP_NAME=your-app-name in Heroku Config Vars)
# heroku_app_name = os.environ.get('HEROKU_APP_NAME')
# if heroku_app_name:
#     ALLOWED_HOSTS.append(f"{heroku_app_name}.herokuapp.com")


# --- Application definition ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'whitenoise.runserver_nostatic', # For serving static files in dev without collectstatic
    'django.contrib.staticfiles',

    # Third-Party Apps
    'rest_framework',
    'corsheaders',

    # Your Apps
    'recommendations', # Your recommendations app
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Whitenoise - Place high up, after SecurityMiddleware
    'corsheaders.middleware.CorsMiddleware', # CORS - Place before CommonMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'recommendation_engine.urls' # Assumes your project directory is 'recommendation_engine'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [], # Add global template directories here if needed
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

WSGI_APPLICATION = 'recommendation_engine.wsgi.application' # Assumes project directory is 'recommendation_engine'


# --- Database ---
# https://docs.djangoproject.com/en/stable/ref/settings/#databases
# Uses dj-database-url to parse the DATABASE_URL environment variable.
# Defaults to SQLite for easy local development if DATABASE_URL is not set.

DATABASES = {
    'default': dj_database_url.config(
        # Set DATABASE_URL in your environment (e.g., mysql://user:pass@host:port/dbname for PythonAnywhere)
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}', # Local SQLite fallback
        conn_max_age=600 # Optional: Number of seconds database connections should persist
    )
}


# --- Password validation ---
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

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


# --- Internationalization ---
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# --- Static files (CSS, JavaScript, Images) ---
# https://docs.djangoproject.com/en/stable/howto/static-files/
# https://whitenoise.evans.io/

STATIC_URL = '/static/'

# Directory where `collectstatic` will gather static files for deployment.
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Whitenoise storage backend ensures files are served efficiently in production.
# Handles compression and adds unique hashes to filenames for caching.
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# --- Default primary key field type ---
# https://docs.djangoproject.com/en/stable/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# --- Django REST Framework Settings ---
# https://www.django-rest-framework.org/api-guide/settings/

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        # Add BrowsableAPIRenderer only during development for easier API testing in browser
        # Conditionally added below based on DEBUG setting
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    # Authentication and Permissions can be added globally here later if needed
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        # By default, allow any request. Change this if you add authentication.
        'rest_framework.permissions.AllowAny',
    ],
}

# Add Browsable API only in development for convenience
if DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')


# --- CORS (Cross-Origin Resource Sharing) Settings ---
# https://github.com/adamchainz/django-cors-headers

# Define origins allowed to make requests to your API.
CORS_ALLOWED_ORIGINS = [
    # Local development frontend
    "http://localhost:8080", # Default Vue CLI port
    "http://127.0.0.1:8080",
    "http://localhost:5173", # Default Vite port (just in case)
    "http://127.0.0.1:5173",
]

# Add the production frontend URL from an environment variable
# Set FRONTEND_URL=https://your-netlify-app.netlify.app (or Vercel URL) in your production environment
frontend_url = os.environ.get('FRONTEND_URL')
if frontend_url:
    CORS_ALLOWED_ORIGINS.append(frontend_url)

# If you need to allow credentials (like cookies or authorization headers)
# CORS_ALLOW_CREDENTIALS = True

# You can also specify allowed methods or headers if needed
# CORS_ALLOW_METHODS = [...]
# CORS_ALLOW_HEADERS = [...]

# For dynamic preview URLs (e.g., Netlify deploy previews), consider using regex:
# CORS_ALLOWED_ORIGIN_REGEXES = [
#     r"^https://\w+--your-netlify-app-name\.netlify\.app$",
# ]