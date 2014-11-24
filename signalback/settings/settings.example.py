# Choose one of these:
# from .deployments.settings_dev import *
# from .deployments.settings_prod import *

# Make this unique, and don't share it with anybody.
SECRET_KEY = ''

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_SECURE_URLS = False       # use http instead of https
AWS_QUERYSTRING_AUTH = False     # don't add complex authentication-related query parameters for requests
AWS_S3_ACCESS_KEY_ID = ''     # enter your access key id
AWS_S3_SECRET_ACCESS_KEY = '' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = ''