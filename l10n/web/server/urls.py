from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^l10n/', include("simple_l10n.urls")),
)
