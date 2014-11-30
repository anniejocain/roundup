# Our settings.py file is nothing more than an
# import for our local settings we don't want
# git to track.

try:
    from .local_settings import *
except ImportError, e:
    print "Using prodcution settings since I'm unable to find local_settings.py"
    
    # Let's assume we're deploying to heroku
    from .deployments.settings_prod import *