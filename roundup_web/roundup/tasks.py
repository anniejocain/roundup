from __future__ import absolute_import

from celery import shared_task


@shared_task
def get_gallery_images(target_url):
    """
    This funciton accepts a url and will create a gallery of images that 
    might represent that URL
    """
    
    # get a url
    # when we get images back, write them to a temp media store
    # update a temp model with them (we might want to make this a redis thing later)
    # once we the user chooses one, we can put that in permanent media store and 
    # update the item's model db with that image
    
    
    
    # Get an png capture from our preview app
    
    # Get the twitter card image
    
    # Get the facebook OG image
    
    # Get the first n images using beautiful soup
    
    print 'done'
    
