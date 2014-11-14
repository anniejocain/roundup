import logging
from roundup.models import Organization, BookmarkletKey, Item

from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@login_required
def landing(request):
    """The dashboard landing page"""

    org = Organization.objects.get(user=request.user)
    contributors = BookmarkletKey.objects.all().filter(organization=org).count()

    context = {'organization': org, 'contributors': contributors}
               
    context = RequestContext(request, context)
    
    return render_to_response('dashboard/dashboard.html', context)


@login_required
def generate_key(request):
    """Generate a bookmarklet key to hand out"""

    org = Organization.objects.get(user=request.user)
    displayKey = None
    bookmarkletLink = None
    
    if request.method == "POST":
        invite_email = request.POST.get('invite_email', '')
        bookmarkletKey = BookmarkletKey(organization=org)
        bookmarkletKey.email = invite_email
        
        bookmarkletKey.save()
        displayKey = bookmarkletKey.key
        
        host = request.get_host()
        bookmarkletLink = 'http://{host}/install-bookmarklet/{bookmarklet_key}'.format(host=host ,bookmarklet_key=displayKey)

        if settings.DEBUG == False:
            host = settings.HOST
        
        content = '''{organization} has invited you to contribute links. Install a bookmarklet here.
            
http://{host}/install-bookmarklet/{bookmarklet_key}
                    
Go for it!
                
'''.format(organization=org.name, host=host ,bookmarklet_key=displayKey)
        
        logger.debug(content)
        
        send_mail(
            "You're invited to contribute links",
            content,
            request.user.email,
            [invite_email], fail_silently=False
        )
    
    context = {'user': request.user, 'bookmarkletLink': bookmarkletLink}
               
    context = RequestContext(request, context)
    
    return render_to_response('dashboard/generate_key.html', context)
    

def display_items(request, slug):
    """Display links"""

    context = {'org_slug': slug}

    context = RequestContext(request, context)

    return render_to_response('items.html', context)

