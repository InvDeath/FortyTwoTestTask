from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.hello.views.home', name='home'),
    url(r'^requests/$', 'apps.hello.views.requests', name='requests'),
    url(r'^contacts_edit/(?P<id>\d+)/$', 'apps.hello.views.contacts_edit',
        name='contacts_edit'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += staticfiles_urlpatterns()
