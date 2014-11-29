# Our settings.py file is nothing more than an
# import for our local settings we don't want
# git to track.

try:
    from .local_settings import *
except ImportError, e:
    print "Unable to find local_settings.py file."
    
    # Let's assume we're deploying to heroku
    from .deployments.settings_prod import *