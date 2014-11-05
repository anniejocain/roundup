from roundup.models import Item, BookmarkletKey
from roundup.forms import (
    AddItemForm,
)

import logging

from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

logger = logging.getLogger(__name__)


def landing(request):
    """Our main landing page"""

    context = {}
               
    context = RequestContext(request, context)
    
    return render_to_response('landing.html', context)
    
    
def add_item(request):

    bookmarklet_key_id = request.GET.get('bookmarklet_key', '')
    bookmarklet_key = BookmarkletKey.objects.get(key=bookmarklet_key_id)
    title = request.GET.get('title', '')
    link = request.GET.get('link', '')
    description = request.GET.get('description', '')
    contributor = request.GET.get('contributor', '')
    
    if request.method == 'POST':
        add_form = AddItemForm(request.POST,)
        
        if add_form.is_valid():
            item = add_form.save(commit=False)
            item.bookmarklet_key = bookmarklet_key
            item.save()
            
            return HttpResponseRedirect(reverse('common_landing'))    
        else:
            context = {'add_form': add_form,} 
            context = RequestContext(request, context)
            return render_to_response('add_item.html', context)
    
    else:
        form_data = {'title':title, 
                'link':link,
                'description':description,
                'contributor':contributor}
        add_form = AddItemForm(initial=form_data)
    
        context = {'add_form': add_form,}           
        context = RequestContext(request, context)
    
        return render_to_response('add_item.html', context)