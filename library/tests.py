from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Book

class BookModelTest(TestCase):
    def test_book_string_representation(self):
        book = Book.objects.create(
            title="Test Book", 
            author="Test Author", 
            published_date="2020-01-01", 
            genre="fiction"
        )
        self.assertEqual(str(book), "Test Book by Test Author")

class BookValidationTest(TestCase):
    def test_future_published_date_validation(self):
        book = Book(
            title="Future Book",
            author="Author",
            published_date="2027-01-01",
            genre="fiction"
        )
        with self.assertRaises(ValidationError):
            book.full_clean()

class BookAPITest(APITestCase):
    def test_create_book_api(self):
        data = {
            "title": "API Test Book",
            "author": "API Author",
            "published_date": "2020-01-01",
            "genre": "mystery"
        }
        response = self.client.post('/api/books/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
