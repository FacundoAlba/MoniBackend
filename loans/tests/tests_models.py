from django.test import TestCase
from loans.models import LoanRequest
from django.core.exceptions import ValidationError
from django.utils import timezone

class LoanRequestModelTest(TestCase):

    def setUp(self):
        self.valid_dni = '12345678'
        self.invalid_dni = '123456789'
        self.full_name = 'John Doe'
        self.gender = 'Male'
        self.valid_email = 'test@example.com'
        self.invalid_email = 'invalid-email'
        self.valid_amount = 50000.00
        self.invalid_amount = 1000001.00
        self.current_time = timezone.now()

    def test_valid_loan_request(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        loan.save()
        self.assertEqual(LoanRequest.objects.count(), 1)
        self.assertEqual(loan.full_name, self.full_name)

    def test_invalid_dni(self):
        loan = LoanRequest(
            dni=self.invalid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_blank_dni(self):
        loan = LoanRequest(
            dni='',
            full_name=self.full_name,
            gender=self.gender,
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_invalid_email(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email=self.invalid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_blank_email(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email='',
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_invalid_amount(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email=self.valid_email,
            amount=self.invalid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_blank_full_name(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name='',
            gender=self.gender,
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_blank_gender(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender='',
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        with self.assertRaises(ValidationError):
            loan.full_clean()

    def test_str_method(self):
        loan = LoanRequest(
            dni=self.valid_dni,
            full_name=self.full_name,
            gender=self.gender,
            email=self.valid_email,
            amount=self.valid_amount,
            created_at=self.current_time
        )
        self.assertEqual(str(loan), self.full_name)
