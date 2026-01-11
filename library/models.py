from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

GENRE_CHOICES = [
    ('fiction', 'Fiction'),
    ('non_fiction', 'Non-Fiction'),
    ('mystery', 'Mystery'),
    ('science', 'Science'),
    ('biography', 'Biography'),
]

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    published_date = models.DateField()
    genre = models.CharField(max_length=20, choices=GENRE_CHOICES)
    is_available = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def clean(self):
        # No future dates!
        if self.published_date > timezone.now().date():
            raise ValidationError('Published date cannot be in future!')

    def __str__(self):
        return f"{self.title} by {self.author}"
