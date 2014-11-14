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