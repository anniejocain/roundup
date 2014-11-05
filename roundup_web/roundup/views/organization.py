from roundup.models import Organization, BookmarkletKey

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.sites.models import Site


def generate_key(request):
    """Generate a bookmarklet key to hand out"""

    if not request.user.is_authenticated():
        return HttpResponseRedirect(reverse('auth_login'))

    org = Organization.objects.get(user=request.user)
    displayKey = None
    
    if request.method == "POST":
        bookmarkletKey = BookmarkletKey(organization=org)
        
        bookmarkletKey.save()
        displayKey = bookmarkletKey.key
    
    context = {'user': request.user, 'displayKey': displayKey}
               
    context = RequestContext(request, context)
    
    return render_to_response('organization/generate_key.html', context)
    
    
def install_bookmarklet(request, bookmarklet_key_id):

    bookmarklet_key = BookmarkletKey.objects.get(key=bookmarklet_key_id)
    organization = bookmarklet_key.organization
    bookmarklet_domain = Site.objects.get_current().domain

    context = {'bookmarklet_key': bookmarklet_key_id, 'organization': organization, 'bookmarklet_domain': bookmarklet_domain}
               
    context = RequestContext(request, context)
    
    return render_to_response('organization/install_bookmarklet.html', context)