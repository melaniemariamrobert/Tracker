from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from django.contrib import admin
from Track.views import home
from Tracker import settings

admin.autodiscover()

# urlpatterns = [
#     url(r'^$', home, name='home') + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
# ]

urlpatterns = patterns('',
    # Examples:
    url(r'^$', home, name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
