from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse

from places.models import Place


class AddPostTestCase(TestCase):
    fixtures = ['places_place.json', 'auth_user.json']

    def setUp(self):
        self.user, created = get_user_model().objects.get_or_create(username='test_user')
        self.user.set_password('12345')
        self.user.save()

        self.place = Place.objects.create(
            user=self.user, title='Test Place', comment='This is a test comment', locations=Point(55.7558, 37.6176)
        )

    def test_add_post(self):
        """Проверка добавления поста"""
        self.client.force_login(self.user)
        form_data = {
            'title': 'Test title',
            'comment': 'This is test comment',
            'locations': 'SRID=4326;POINT (90.49912261543795 56.25105638373618)',
        }
        path = reverse('places:create')
        response = self.client.post(path, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Place.objects.filter(title='Test title').exists())
        new_post = Place.objects.get(title='Test title')
        self.assertEqual(new_post.comment, 'This is test comment')

    def test_edit_post(self):
        """Проверка редактирования поста"""
        self.client.force_login(self.user)
        form_data = {
            'title': 'New test title',
            'comment': 'This is new test comment',
            'locations': 'SRID=4326;POINT (55.49912261543795 30.25105638373618)',
        }
        path = reverse('places:edit', kwargs={'pk': self.place.id})
        response = self.client.post(path, form_data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Place.objects.filter(title='New test title').exists())
        new_post = Place.objects.get(title='New test title')
        self.assertEqual(new_post.comment, 'This is new test comment')

    def tearDown(self):
        self.user.delete()
