from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from config import settings
from places.views import page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls', namespace='places')),
    path('accounts/', include('allauth.urls')),
    path('logout/', include('users.urls', namespace='users')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = page_not_found
