from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from web.models import Image


class MyImagesViewTestClass(TestCase):
    def setUp(self):
        test_user1 = User.objects.create_user(
            username='testuser1', password='1X<ISRUkw+tuK')
        test_user2 = User.objects.create_user(
            username='testuser2', password='2HJ1vRV0Z&3iD')
        test_user1.save()
        test_user2.save()

        for i in range(2):
            Image.objects.create(
                user=test_user1, title="user1 image "+str(i), file="static/images/favicon.png")
            Image.objects.create(
                user=test_user2, title="user2 image "+str(i), file="static/images/favicon.png")

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('accounts:my_images'))
        self.assertRedirects(response, '/accounts/login?next=/accounts/')

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:my_images'))
        self.assertTemplateUsed(response, 'accounts/user_images.html')

    def test_images_belong_to_logged_in_user(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('accounts:my_images'))
        for image in response.context['images']:
            self.assertEqual(image.user.username, "testuser1")
