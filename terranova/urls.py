from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), 
    path('admin/', admin.site.urls),
    path('hizmetler/', include('hizmetler.urls')),
    path('etkinlikler/', include('etkinlikler.urls')),
    path('bloglar/', include('bloglar.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
