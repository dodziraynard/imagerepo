from django.test import TestCase
from web.forms import ImageForm


class ImageFormTestClass(TestCase):
    def test_image_form_title_attr(self):
        form = ImageForm()
        self.assertTrue("title" in form.fields)

    def test_image_form_user_tags_attr(self):
        form = ImageForm()
        self.assertTrue("user_tags" in form.fields)
