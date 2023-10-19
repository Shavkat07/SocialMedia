from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="MRIT API",
        default_version='v1',
        description="MRTI rest api documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="alhppypro@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticated,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]

urlpatterns += i18n_patterns(
    path('blog/api/', include(('blog.urls', 'blog'), namespace='blog')),
    path('employee/api/', include(('employe.urls', 'employe'), namespace='employe')),
    path('portfolio/api/', include(('portfolio.urls', 'portfolio'), namespace='portfolio'))
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
