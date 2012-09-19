from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'number/(?P<number>.*)$', 'simple_l10n.views.number', 
        name='l10n_number'),
)

