from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView


urlpatterns = patterns('roundup.views',

    # Common Pages
    url(r'^/?$', 'common.landing', name='common_landing'),
)
