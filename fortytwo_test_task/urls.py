from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns(
    '',
    # Examples:
    url(r'^$', 'apps.hello.views.contacts', name='home'),
    url(r'^requests/$', 'apps.hello.views.requests', name='requests'),
    url(r'^contacts_edit/(?P<id>\d+)/$', 'apps.hello.views.contacts_edit',
        name='contacts_edit'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
