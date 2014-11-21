from roundup.models import Item, BookmarkletKey, Organization, ImageGallery, ItemImage
from roundup.forms import (
    AddItemForm,
)
from roundup.tasks import get_twitter_card_image, get_screen_capture

import logging
import requests

from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.contrib.sites.models import Site
from django.core import serializers

logger = logging.getLogger(__name__)


def landing(request):
    """Our main landing page"""

    context = {}
               
    context = RequestContext(request, context)
    
    return render_to_response('landing.html', context)
    
    
def _get_gallery_images(image_gallery_id, target_url):
    """
    A helper function to call all of our async image gathering tasks
    """
    
    # Get our markup
    markup = requests.get(target_url).text
    
    # Get twitter image
    get_twitter_card_image.delay(image_gallery_id, target_url, markup)
    
    # Get a screen capture of the page
    get_screen_capture.delay(image_gallery_id, target_url, markup)
        
    # Get the facebook open graph image
    
    # Get the first n images on the page

    
    
def add_item(request):

    bookmarklet_key_id = request.GET.get('bookmarklet_key', '')
    bookmarklet_key = BookmarkletKey.objects.get(key=bookmarklet_key_id)
    organization = bookmarklet_key.organization
    title = request.GET.get('title', '')
    link = request.GET.get('link', '')
    description = request.GET.get('description', '')
    contributor = bookmarklet_key.display_name
    
    if request.method == 'POST':
        add_form = AddItemForm(request.POST,)
        
        if add_form.is_valid():
            bookmarklet_key.display_name = add_form.cleaned_data['contributor']
            bookmarklet_key.save()
            item = add_form.save(commit=False)
            item.bookmarklet_key = bookmarklet_key
            item.save()
            
            return HttpResponseRedirect(reverse('dashboard_display_items', kwargs={'slug' : organization.slug}))   
        else:
            context = {'add_form': add_form,} 
            context = RequestContext(request, context)
            return render_to_response('add_item.html', context)
    
    else:
        
        # Start gathering our images
        image_gallery = ImageGallery()
        image_gallery.save()
        _get_gallery_images(image_gallery.id, link)
        
        form_data = {'title':title, 
                'link':link,
                'description':description,
                'contributor':contributor}
        add_form = AddItemForm(initial=form_data)
    
        context = {'add_form': add_form, 'organization': organization}           
        context = RequestContext(request, context)
    
        return render_to_response('add_item.html', context)
        
        
def install_bookmarklet(request, bookmarklet_key_id):

    try:
        bookmarklet_key = BookmarkletKey.objects.get(key=bookmarklet_key_id)
    except BookmarkletKey.DoesNotExist:
        raise Http404
        
    organization = bookmarklet_key.organization
    bookmarklet_domain = Site.objects.get_current().domain

    context = {'bookmarklet_key': bookmarklet_key_id, 'organization': organization, 'bookmarklet_domain': bookmarklet_domain}
               
    context = RequestContext(request, context)
    
    return render_to_response('install_bookmarklet.html', context)
    
    
def get_gallery(request):

    gallery_id = request.GET.get('gallery_id', '')

    gallery_images = ItemImage.objects.filter(image_gallery__id=gallery_id)
    
    data = serializers.serialize('json', gallery_images)
    return HttpResponse(data, mimetype='application/json')