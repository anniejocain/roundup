from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf


def landing(request):
    """Our main landing page"""

    context = {}
               
    context = RequestContext(request, context)
    
    return render_to_response('landing.html', context)