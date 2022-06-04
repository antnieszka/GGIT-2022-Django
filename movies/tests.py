from datetime import datetime
from django.test import TestCase

from .models import Movie

# Create your tests here.
class TestMovies(TestCase):
    def setUp(self):
        Movie.objects.create(title="test", published_at=datetime.now())

    def test_true(self):
        assert True

    def test_movie_count(self):
        assert Movie.objects.count() == 1

    def test_movie_get(self):
        assert Movie.objects.get(title="test")
