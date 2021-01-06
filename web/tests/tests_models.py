from django.test import TestCase
from web.models import Image


class ImageModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        Image.objects.create(
            title="My image", auto_tags="car forest", user_tags="taxi farm")

    def setUp(self):
        self.img = Image.objects.first()

    def test_image_table_name(self):
        db_table = self.img._meta.db_table
        self.assertEqual(db_table, 'images')

    def test_image_has_user_attr(self):
        self.assertTrue(hasattr(self.img, "user"))

    def test_image_has_title_attr(self):
        self.assertTrue(hasattr(self.img, "title"))

    def test_image_has_user_tags_attr(self):
        self.assertTrue(hasattr(self.img, "user_tags"))

    def test_image_has_auto_tags_attr(self):
        self.assertTrue(hasattr(self.img, "auto_tags"))

    def test_image_has_time_stamp_attr(self):
        self.assertTrue(hasattr(self.img, "time_stamp"))

    def test_image_has_file_attr(self):
        self.assertTrue(hasattr(self.img, "file"))

    def test_image_has_is_public_attr(self):
        self.assertTrue(hasattr(self.img, "is_public"))

    def test_image_tags(self):
        self.assertEqual(self.img.tags,  ["car", "forest", "taxi", "farm"])
