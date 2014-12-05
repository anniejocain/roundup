from items.models import Item

from django.conf.urls import url

from tastypie.utils import trailing_slash
from tastypie.resources import ModelResource

class ItemResource(ModelResource):
    """
    The API for our Item model. The search piece is likely
    the thing that's of most interest. It allows for the flitering of links
    based on the organization's slug
    """
    
    class Meta:
        queryset = Item.objects.all()
        resource_name = 'item'        

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (self._meta.resource_name, 
                trailing_slash()), self.wrap_view('get_search'), name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        
        # TODO: Use the tastypie/django pagination stuff to handle this.
        # there has to be a good tastypie pattern for this
        org_slug = request.GET.get('q', '')
        objects = Item.objects.filter(bookmarklet_key__organization__slug=org_slug).order_by('-contributed_date')[:200]
        
        object_list = []
        for o in objects:
            
            
            thumbnail = ''
            if o.itemimage_set.first():
                thumbnail = o.itemimage_set.first().item_image.url
            
            stripped_object = { 'title': o.title,
                                'description': o.description,
                                'link': o.link,
                                'contributor': o.contributor,
                                'contributed_date': o.contributed_date,
                                'thumbnail': thumbnail,
                                }
            object_list.append(stripped_object)

        return self.create_response(request, object_list)