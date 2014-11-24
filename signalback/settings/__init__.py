try:
    from .settings import *
except ImportError, e:
    if e.message=='No module named settings':
        from .deployments.settings_dev import *
    else:
        raise
