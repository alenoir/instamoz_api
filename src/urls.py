from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from apps.instapix.views import MosaicPreview, MosaicRealtime, MosaicList, MosaicDetail


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Instamoz.views.home', name='home'),
    url(r'^', include('apps.instapix.urls')),
    url(r'^mosaics/(?P<mosaic_id>\d)/preview$', MosaicPreview.as_view()),
    url(r'^realtime-instagram/$', MosaicRealtime.as_view()),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^mosaics/$', MosaicList.as_view()),
    url(r'^mosaics/(?P<pk>[0-9]+)/$', MosaicDetail.as_view()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
