from django.conf.urls.defaults import patterns, url

from foirequest.feeds import FoiRequestFeed, FoiRequestFeedAtom


urlpatterns = patterns("",
    url(r"^(?P<slug>[-\w]+)/$", 'foirequest.views.show', name="foirequest-show"),
    url(r"^(?P<slug>[-\w]+)/feed/$", FoiRequestFeedAtom(), name="foirequest-feed_atom"),
    url(r"^(?P<slug>[-\w]+)/rss/$", FoiRequestFeed(), name="foirequest-feed"),
    url(r"^(?P<slug>[-\w]+)/suggest/public-body/$", 'foirequest.views.suggest_public_body', name="foirequest-suggest_public_body"),
    url(r"^(?P<slug>[-\w]+)/set/public-body/$", 'foirequest.views.set_public_body', name="foirequest-set_public_body"),
    url(r"^(?P<slug>[-\w]+)/set/status/$", 'foirequest.views.set_status', name="foirequest-set_status"),
    url(r"^(?P<slug>[-\w]+)/send/message/$", 'foirequest.views.send_message', name="foirequest-send_message"),
    url(r"^(?P<slug>[-\w]+)/make/public/$", 'foirequest.views.make_public', name="foirequest-make_public"),
)