from settings_common import *
import dj_database_url


DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (
    'storages',
)


DATABASES['default'] = dj_database_url.config()

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = ''     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = '' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = ''