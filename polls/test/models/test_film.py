from django.test import TestCase

from polls.models import Film


class Test(TestCase):

    def setUp(cls):
        Film.objects.create(id=1, Title="film1", Year=2021)
        Film.objects.create(id=2, Title="film2", Year=2020)
        Film.objects.create(id=3, Title="film3", Year=2021)
        Film.objects.create(id=4, Title="film4", Year=2020)
        Film.objects.create(id=5, Title="film5", Year=2021)

    ###########################
    # Tests for next method
    ###########################

    def test_next_positive(self):
        # when
        nextId = Film.objects.get(id=1).next()
        # then
        self.assertEqual(2, nextId)

    def test_next_with_gap(self):
        # when
        nextId = Film.objects.get(id=2).next()
        # then
        self.assertEqual(4, nextId, "3 has year 2021 -< skip")

    def test_next_last(self):
        # when
        nextId = Film.objects.get(id=5).next()
        # then
        self.assertEqual(-1, nextId)

    def test_next_last_with_gap(self):
        # when
        nextId = Film.objects.get(id=4).next()
        # then
        self.assertEqual(-1, nextId, "5 has year 2021 -< skip")

    ###########################
    # Tests for previous method
    ###########################

    def test_prev_positive(self):
        # when
        prevId = Film.objects.get(id=3).previous()
        # then
        self.assertEqual(2, prevId)

    def test_prev_with_gap(self):
        # when
        prevId = Film.objects.get(id=4).previous()
        # then
        self.assertEqual(2, prevId, "3 has year 2021 -< skip")

    def test_prev_first(self):
        # when
        prevId = Film.objects.get(id=1).previous()
        # then
        self.assertEqual(-1, prevId)

    def test_prev_first_with_gap(self):
        # when
        prevId = Film.objects.get(id=2).previous()
        # then
        self.assertEqual(-1, prevId, "1 has year 2021 -< skip")
