from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from loans.models import LoanRequest

class UserTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.signin_url = reverse('signin')
        self.signout_url = reverse('logout')
        self.loans_url = reverse('loans')
        self.user_detail_url = reverse('user')

        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }

        self.user = User.objects.create_user(username='existinguser', password='password123')

    def test_signup_view(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_signup_view_existing_user(self):
        response = self.client.post(self.signup_url, {
            'username': 'existinguser',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Stays on signup page
        self.assertContains(response, '* El Usuario ya existe')

    def test_signin_view(self):
        response = self.client.post(self.signin_url, {
            'username': 'existinguser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful signin

    def test_signin_view_invalid_credentials(self):
        response = self.client.post(self.signin_url, {
            'username': 'nonexistentuser',
            'password': 'password123',
        })
        self.assertEqual(response.status_code, 200)  # Stays on signin page
        self.assertContains(response, "* Usuario o Contraseña incorrecto")

    def test_signout_view(self):
        self.client.login(username='existinguser', password='password123')
        response = self.client.get(self.signout_url)
        self.assertEqual(response.status_code, 302)  # Redirects after signout

    def test_user_detail_view_get(self):
        self.client.login(username='existinguser', password='password123')
        response = self.client.get(self.user_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'existinguser')

    def test_user_detail_view_post(self):
        self.client.login(username='existinguser', password='password123')
        response = self.client.post(self.user_detail_url, {
            'username': 'newusername',
            'password1': 'newpassword123',
            'password2': 'newpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful update
        self.assertTrue(User.objects.filter(username='newusername').exists())

    def test_loans_view(self):
        self.client.login(username='existinguser', password='password123')
        LoanRequest.objects.create(
            dni='12345678',
            full_name='John Doe',
            gender='M',
            email='john@example.com',
            amount=1000,
            loan_status='approve'
        )
        response = self.client.get(self.loans_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'John Doe')

class LoanRequestTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')

    def test_create_loan_request(self):
        loan_request = LoanRequest.objects.create(
            dni='12345678',
            full_name='John Doe',
            gender='M',
            email='john@example.com',
            amount=1000,
            loan_status='approve'
        )
        self.assertEqual(str(loan_request), 'John Doe')
        self.assertEqual(loan_request.loan_status, 'approve')
