# Choose one of these:
# from .deployments.settings_dev import *
# from .deployments.settings_prod import *

#### Stuff needed for the Heroku deploy - start ####
# We have a fab command to tack this stuff onto settings.py for heroku
SECRET_KEY = ''

MEDIA_ROOT = "/Users/your-username/dev_area/signalback/srv/media/"
MEDIA_URL = "/media/"
STATIC_URL = "/static/" 

#### Stuff needed for the Heroku deploy - start ####
# We have a fab command to tack this stuff onto settings.py for heroku
SECRET_KEY = ''

AWS_ACCESS_KEY_ID = ''     # enter your access key id
AWS_SECRET_ACCESS_KEY = '' # enter your secret access key
AWS_STORAGE_BUCKET_NAME = ''
S3_URL = 'http://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME
#### Stuff needed for the Heroku deploy - end ####