from django.contrib import admin
from django.contrib.gis import admin

from .models import Place


@admin.register(Place)
class PlaceAdmin(admin.GISModelAdmin):
    fields = ['user', 'title', 'comment', 'locations']
    list_display = ('user', 'title', 'comment', 'locations', 'time_create', 'time_update')
    list_filter = ('time_create',)
    search_fields = ('title',)