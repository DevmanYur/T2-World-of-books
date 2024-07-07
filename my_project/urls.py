from django.contrib import admin
from django.urls import path, include

from my_app import views

# добавлено для показа картинок
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('my_app.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
