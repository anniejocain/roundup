import os
from settings_common import *
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)

DATABASES['default'] = dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
#import os
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#STATIC_ROOT = 'staticfiles'
#STATIC_URL = '/static/'

#STATICFILES_DIRS = (
#    os.path.join(BASE_DIR, 'static'),
#)


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests

# Let's look to the heroku confiv vars (env vars) for the rest of our prod settings
AWS_S3_ACCESS_KEY_ID = 'AWS_S3_ACCESS_KEY_ID' in os.environ # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = 'AWS_S3_SECRET_ACCESS_KEY' in os.environ # AWS_S3_SECRET_ACCESS_KEY = '' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME' in os.environ # AWS_STORAGE_BUCKET_NAME = ''

SECRET_KEY = 'SECRET_KEY' in os.environ


STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL