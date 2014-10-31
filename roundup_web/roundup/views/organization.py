from roundup.models import Organization, BookmarkletKey

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf


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