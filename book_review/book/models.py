from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


class Book(models.Model):

    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Science Fiction', 'Science Fiction'),
        ('Biography', 'Biography'),
        ('Mystery', 'Mystery'),
        ('Fantasy', 'Fantasy'),
        ('Other', 'Other'),
    ]

    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=50)
    published_date = models.DateField()
    isbn_number = models.CharField(max_length=20, unique=True)
    description = models.TextField(max_length=1000)
    average_rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)], default=0.0)

    def __str__(self):
        return self.title