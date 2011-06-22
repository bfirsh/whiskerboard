from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from board.models import Event

class EventFeed(Feed):
    description = "Latest status updates."
    link = '/'
    feed_type = Atom1Feed
    
    def title(self):
        return Site.objects.get_current().name

    def items(self):
        return Event.objects.order_by('-start')[:25]

    def item_title(self, item):
        if item.informational:
            status = 'Information'
        else:
            status = item.status.name
        return '%s: %s' % (item.service.name, status)

    def item_description(self, item):
        return item.message

    def item_link(self, item):
        return item.service.get_absolute_url()


