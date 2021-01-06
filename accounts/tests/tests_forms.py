from django.test import TestCase
from accounts.forms import UserForm


class UserFormTestClass(TestCase):
    def test_user_form_username_attr(self):
        form = UserForm()
        self.assertTrue("username" in form.fields)
