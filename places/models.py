from django.contrib.auth import get_user_model
from django.contrib.gis.db import models


class Place(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, verbose_name='Пользователь', related_name='places'
    )
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    comment = models.TextField(blank=True, verbose_name='Комментарий')
    locations = models.PointField(verbose_name='Местоположение')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural = 'Места'
        ordering = ['-time_create']


    def __str__(self):
        return self.title
