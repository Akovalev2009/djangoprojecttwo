INSTALLED_APPS = [
    ...
    'django.contrib.sites',
    'django.contrib.flatpages',
    'myapp',
    ...
]

MIDDLEWARE = [
    ...
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    ...
]

SITE_ID = 1

STATIC_URL = '/static/'

# settings.py

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "myapp/static",
]
