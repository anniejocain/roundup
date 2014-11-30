# Choose one of these:
# from .deployments.settings_dev import *
# from .deployments.settings_prod import *

#### Stuff needed for the Heroku deploy - start ####
# We have a fab command to tack this stuff onto settings.py for heroku
SECRET_KEY = ''

AWS_ACCESS_KEY_ID = ''     # enter your access key id
AWS_SECRET_ACCESS_KEY = '' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = ''

S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
STATIC_URL = S3_URL

# swap this to cleardb
HEROKU_DATABASES = {
    'default': {
        'ENGINE': '', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
#### Stuff needed for the Heroku deploy - end ####