try:
    from .settings import *
except ImportError, e:
    print "Unable to find settings.py file."
    if e.message=='No module named settings':
        from .deployments.settings_prod import *
    else:
        raise
