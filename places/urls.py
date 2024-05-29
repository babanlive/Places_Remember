from django.urls import path

from . import views


app_name = 'places'

urlpatterns = [
    path ('', views.IndexView.as_view(), name='index'),
    path('home/', views.HomeView.as_view(), name='home'),
    path('new/', views.CreatePlace.as_view(), name='create'),
    path('edit/<int:pk>', views.EditPlace.as_view(), name='edit'),
]
