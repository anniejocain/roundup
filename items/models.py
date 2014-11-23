from django.contrib.auth.models import User
from django.db import models

import uuid


class Organization(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=400)
    slug = models.SlugField(unique=True)
    public_link = models.URLField(max_length=2000, null=True, blank=True)
    public_email = models.EmailField(max_length=254, null=True, blank=True)
    
    def __unicode__(self):
        return self.name
        

class BookmarkletKey(models.Model):
    organization = models.ForeignKey(Organization)
    key = models.CharField(max_length=255, null=False, blank=False, primary_key=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    display_name = models.CharField(max_length=400, null=True, blank=True)
    
    def save(self, *args, **kwargs):
        """
        We need a unique key for each bookmarklet. Let's create that key
        when we create a new bookmarklet entry in the DB
        """

        if not self.key:
            generated_key = uuid.uuid4()
            self.key = str(generated_key)
            super(BookmarkletKey, self).save(*args, **kwargs)
            
    def __unicode__(self):
        return self.key
        
    
class Item(models.Model):
    bookmarklet_key = models.ForeignKey(BookmarkletKey)
    title = models.CharField(max_length=400)
    description = models.CharField(max_length=117, null=True, blank=True)
    link = models.URLField(max_length=2000, null=True, blank=True)
    contributor = models.CharField(max_length=400, null=True, blank=True)
    contributed_date = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return self.title

class ImageGallery(models.Model):
    """
    When a user creates a new item we grab a number of images for them
    and present them in an image gallery. Those images are tracked in
    ItemImage. We use this model to group them together. The images
    that aren't selected by the user will be deleted, as will the 
    ImageGallery instance.
    """
    created_date = models.DateTimeField(auto_now=True)
    

class ItemImage(models.Model):
    """
    We want to associate an image with an item. We track that image here.
    """
    item = models.ForeignKey(Item, null=True, blank=True)
    image_gallery = models.ForeignKey(ImageGallery, null=True, blank=True)
    item_image = models.ImageField(upload_to='item_images')