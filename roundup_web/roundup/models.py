from django.contrib.auth.models import User
from django.db import models


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
    
    def __unicode__(self):
        return self.key
        
    
class Item(models.Model):
    bookmarklet_key = models.ForeignKey(BookmarkletKey)
    title = models.CharField(max_length=400)
    link = models.URLField(max_length=2000, null=True, blank=True)
    contributor = models.CharField(max_length=400, null=True, blank=True)
    contributed_date = models.DateTimeField(auto_now=True)
        
    def __unicode__(self):
        return self.title