from __future__ import absolute_import

from roundup.models import ItemImage, ImageGallery

from django.core.files import File
from django.core.files.base import ContentFile

import urllib, json
from urlparse import urlparse

from celery import shared_task
from bs4 import BeautifulSoup
import requests



@shared_task
def get_twitter_card_image(image_gallery_id, target_url, markup):
    """
    This function will see if there is a Twitter Card image associated
    with the URL. If there is, it'll save it to our media store
    and update our gallery model.
    """
    
    # Get our markup. And parse it. This should be moved to a common function
    soup = BeautifulSoup(markup)
    
    if soup.find('meta', {"name": "twitter:image"}):
        twitter_image = soup.find('meta', {"name": "twitter:image"})['content']

        # Get our filename. Isn't there a better way to do this?
        parsed_url = urlparse(twitter_image)
        filename = parsed_url.path.split('/')[-1]
        
        print target_url
        print filename

        # Add the image to our datastore and update the gallery
        image_content = ContentFile(requests.get(twitter_image).content)
        image_gallery = ImageGallery.objects.get(id=image_gallery_id)
        item_image = ItemImage(image_gallery=image_gallery)
        item_image.item_image.save(filename, image_content)
        item_image.save()
        

@shared_task
def get_screen_capture(image_gallery_id, target_url, markup):
    """
    This function will get a screen capture of the page from our
    preview service. Then, it'll save it to our media store
    and update our gallery model.
    """
    preview_url = 'http://hlslwebtest.law.harvard.edu/preview/create?url=%s' % urllib.quote(target_url)

    response = requests.get(preview_url).text
    serialized_response = json.loads(response)

    preview_url_image = 'http://hlslwebtest.law.harvard.edu%s' % serialized_response['image_url']

    # Get our filename. Isn't there a better way to do this?
    parsed_url = urlparse(preview_url_image)
    filename = parsed_url.path.split('/')[-1]

    # Add the image to our datastore and update the gallery
    image_content = ContentFile(requests.get(preview_url_image).content)
    image_gallery = ImageGallery.objects.get(id=image_gallery_id)
    item_image = ItemImage(image_gallery=image_gallery)
    item_image.item_image.save(filename, image_content)
    item_image.save()