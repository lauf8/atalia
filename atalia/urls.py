from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('apps.home.urls')),
    path('entidade/', include('apps.entidade.urls')),
    path('tesouraria/', include('apps.tesouraria.urls')),
    path('accounts/', include('apps.auth2.urls'))


]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )