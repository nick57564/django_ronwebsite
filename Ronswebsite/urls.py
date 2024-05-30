from django.contrib import admin
from django.urls import path, include
from Base.views import base_view

urlpatterns = [
    path('', base_view, name='base_view'),
    path('admin/', admin.site.urls, name='admin_view'),
    path('fotogalerij/', include('Fotogalerij.urls')),
    path('contact/', include('Contact.urls')),
]
