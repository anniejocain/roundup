from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import patterns, url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView

from roundup.api import ItemResource

item_resource = ItemResource()

urlpatterns = patterns('roundup.views',

    # Common Pages
    url(r'^/?$', 'common.landing', name='common_landing'),
    url(r'^add-item?$', 'common.add_item', name='add_item'),
    url(r'^install-bookmarklet/(?P<bookmarklet_key_id>[a-zA-Z0-9\-]+)/$', 'common.install_bookmarklet', name='common_install_bookmarklet'),
    
    # Organization Pages
    url(r'^dashboard/$', 'dashboard.landing', name='dashboard_landing'),
    url(r'^(?P<slug>[a-zA-Z-]+)/items/?$', 'dashboard.display_items', name='dashboard_display_items'),
    url(r'^dashboard/generate-key/$', 'dashboard.generate_key', name='dashboard_generate_key'),
    
     # Session/account management
    url(r'^password/change/$', auth_views.password_change, {'template_name': 'registration/password_change_form.html'}, name='auth_password_change'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='auth_login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'registration/logout.html'}, name='auth_logout'),
    url(r'^password/change/$', auth_views.password_change, {'template_name': 'registration/password_change_form.html'}, name='auth_password_change'),
    url(r'^password/change/done/$', auth_views.password_change_done, {'template_name': 'registration/password_change_done.html'},   name='auth_password_change_done'),
    url(r'^password/reset/$', auth_views.password_reset, {'template_name': 'registration/password_reset_form.html'}, name='auth_password_reset'),
    url(r'^password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, {'template_name': 'registration/password_reset_confirm.html'}, name='auth_password_reset_confirm'),
    url(r'^password/reset/complete/$', auth_views.password_reset_complete, {'template_name': 'registration/password_reset_complete.html'}, name='auth_password_reset_complete'),
    url(r'^password/reset/done/$', auth_views.password_reset_done, {'template_name': 'registration/password_reset_done.html'}, name='auth_password_reset_done'),

    # Tastypie urls. We might want to move these into their own file
    (r'^api/', include(item_resource.urls)),
)
