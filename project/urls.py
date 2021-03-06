# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from harrastuspassi.urls.api import (
    internal_urlpatterns as api_internal_urlpatterns,
    public_urlpatterns as api_public_urlpatterns,
)

schema_url_patterns = api_public_urlpatterns
if settings.DEBUG:
    schema_url_patterns += api_internal_urlpatterns

admin_urls = [
    path('sysadmin/', admin.site.urls),
]

auth_urls = [
    path('accounts/', include('django.contrib.auth.urls')),
]

app_urls = [
    path('', include('harrastuspassi.urls')),
    path('openapi', get_schema_view(
        title="Harrastuspassi",
        description="API documentation",
        patterns=schema_url_patterns
    ), name='openapi-schema'),
    path('api-documentation/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),
    path('monitor/', include('health_check.urls'))
]

static_urls = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
static_urls += staticfiles_urlpatterns()

urlpatterns = admin_urls + auth_urls + app_urls + static_urls
