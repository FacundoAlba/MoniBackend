from django.test import TestCase
from loans.views import CustomUserCreationForm

class CustomUserCreationFormTests(TestCase):
    def test_form_valid_data(self):
        form = CustomUserCreationForm(data={
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertTrue(form.is_valid())

    def test_form_invalid_data(self):
        form = CustomUserCreationForm(data={
            'username': '',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        })
        self.assertFalse(form.is_valid())