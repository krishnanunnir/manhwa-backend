from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

import web.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("web/", include(web.urls)),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
