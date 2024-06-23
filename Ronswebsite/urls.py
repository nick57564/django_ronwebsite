from django.contrib import admin
from django.urls import path, include
from Base.views import base_view
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', base_view, name='base_view'),
    path('admin/', admin.site.urls, name='admin_view'),
    path('fotogalerij/', include('Fotogalerij.urls')),
    path('contact/', include('Contact.urls')),
]

if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
