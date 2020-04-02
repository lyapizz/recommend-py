from django.test import TestCase
from django.urls import reverse


class FilmIndexViewTests(TestCase):

    def test_no_films(self):
        """
        If no films exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No films are available.")
        self.assertQuerysetEqual(response.context['latest_films_list'], [])
