import logging
from roundup.models import Organization, BookmarkletKey, Item

from django.http import HttpResponseRedirect, Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.db.models import Count
from django.contrib.sites.models import Site
from django.conf import settings
from django.contrib.auth.decorators import login_required

logger = logging.getLogger(__name__)


@login_required
def landing(request):
    """The dashboard landing page"""

    org = Organization.objects.get(user=request.user)
    contributors = BookmarkletKey.objects.all().filter(organization=org).annotate(items=Count('item',distinct=True)).order_by('email')
    items = Item.objects.all().filter(bookmarklet_key__organization=org).count()
    contributors_count = contributors.count()

    context = {'organization': org, 'contributors': contributors, 'items': items, 'contributors_count': contributors_count}
    
    if request.method == 'POST':
        bookmarklet_key = BookmarkletKey.objects.get(key=request.POST.get("bookmarklet_key_id", ""))
        if bookmarklet_key.is_active == True:
            bookmarklet_key.is_active = False
        else:
            bookmarklet_key.is_active = True
        logger.debug(bookmarklet_key.is_active)
        bookmarklet_key.save()
               
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

