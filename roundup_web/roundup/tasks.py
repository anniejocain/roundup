from __future__ import absolute_import

from celery import shared_task


@shared_task
def get_gallery_images(target_url):
    """
    This funciton accepts a url and will create a gallery of images that 
    might represent that URL
    """
    
    # Get an png capture from our preview app
    
    # Get the twitter card image
    
    # Get the facebook OG image
    
    # Get the first n images using beautiful soup
    
    print 'done'
    
