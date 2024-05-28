from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('places.urls', namespace='places')),
    path('accounts/', include('allauth.urls')),
    path('logout/', include('users.urls', namespace='users')),
]
