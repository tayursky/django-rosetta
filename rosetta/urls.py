try:
    from django.conf.urls import patterns, url
except ImportError:
    from django.conf.urls.defaults import patterns, url


urlpatterns = patterns('rosetta.views',
    url(r'^rosetta/$', 'home', name='rosetta-home'),
    url(r'^rosetta/pick/$', 'list_languages', name='rosetta-pick-file'),
    url(r'^rosetta/download/$', 'download_file', name='rosetta-download-file'),
    url(r'^rosetta/select/(?P<langid>[\w\-_\.]+)/(?P<idx>\d+)/$', 'lang_sel', name='rosetta-language-selection'),
    url(r'^rosetta/translate/$', 'translate_text', name='translate_text'),
)
