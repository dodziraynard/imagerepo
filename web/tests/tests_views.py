from django.test import TestCase
from django.urls import reverse
from web.models import Image


class IndexViewTestClass(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('web:index'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('web:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/index.html')


class SearchViewTestClass(TestCase):
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('web:search'), {"query": "title"})
        self.assertEqual(response.status_code, 200)

    # Searching with empty query should redirect to the homepage
    def test_view_url_accessible_by_name_redirect(self):
        response = self.client.get(reverse('web:search'))
        self.assertRedirects(response, reverse("web:index"))

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('web:search'), {"query": "title"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/search_view.html')


class ImageDetailViewTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Image.objects.create(title="My title", pk=0,
                             file="static/images/favicon.png")

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('web:image_details', args=[0]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('web:image_details', args=[0]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'web/image_details.html')
