from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('apps.home.urls')),
    path('entidade/', include('apps.entidade.urls')),
    path('tesouraria/', include('apps.tesouraria.urls'))    
]
