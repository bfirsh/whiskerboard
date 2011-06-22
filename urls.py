from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from board.feeds import EventFeed
from board.views import IndexView, ServiceView

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^services/(?P<slug>[-\w]+)$', ServiceView.as_view(), name='service'),
    url(r'^feed$', EventFeed(), name='feed'),

    url(r'^admin/', include(admin.site.urls)),
)
