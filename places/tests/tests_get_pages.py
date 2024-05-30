from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from places.models import Place


class GetPagesTestCase(TestCase):
    fixtures = ['places_place.json', 'auth_user.json']

    def setUp(self):
        self.user = get_user_model().objects.get(pk=1)
        self.user.set_password('12345')
        self.user.save()

    def test_index_page(self):
        """Проверка отображения главной страницы"""
        path = reverse('places:index')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.context_data['title_page'], 'Главная страница')

    def test_redirect_homepage(self):
        """Проверка редиректа на главную страницу"""
        path = reverse('places:home')
        redirect_uri = reverse('places:index') + '?next=' + path
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, redirect_uri)

    def test_available_posts(self):
        """Проверка отображения постов пользователя"""
        self.client.force_login(self.user)
        post_list = Place.objects.filter(user=self.user)
        path = reverse('places:home')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(len(response.context_data['posts']), 5)
        self.assertQuerySetEqual(response.context_data['posts'], post_list[:5])

    def test_available_edit_page(self):
        """Проверка отображения страницы редактирования поста"""
        self.client.force_login(self.user)
        post = Place.objects.get(pk=4)
        path = reverse('places:edit', kwargs={'pk': post.pk})
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['place'].comment, post.comment)

    def tearDown(self):
        self.user.delete()
