
from argparse import Namespace
from xml.dom.minidom import Document
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('store.urls', namespace='store'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,Document_root = settings.MEDIA_ROOT)
