import numpy as np
from django.test import TestCase
from django_registration.forms import User

from polls.actions.actions import collectionToMatrixDict, matrixToCollectionDict, prepareMyPredictions, printTopList
from polls.models import Film


class Test(TestCase):

    def setUp(cls):
        cls._num_users = 4
        cls._num_movies = 5
        cls._num_features = 1

        cls._params = dict()
        cls._params['X'] = np.zeros((cls._num_movies, cls._num_features))
        cls._params['Theta'] = np.zeros((cls._num_users, cls._num_features))
        cls._params['Ymean'] = np.array([[1], [2], [3], [4], [5]])

        User.objects.create(id=1, username='user1')
        User.objects.create(id=3, username='user2')
        User.objects.create(id=4, username='user3')
        User.objects.create(id=99, username='user4')

        Film.objects.create(id=1, Title="film1", Year=2020)
        Film.objects.create(id=2, Title="film2", Year=2020)
        Film.objects.create(id=4, Title="film3", Year=2020)
        Film.objects.create(id=5, Title="film4", Year=2020)
        Film.objects.create(id=66, Title="film5", Year=2020)

    def test_collection_to_matrix_dict(self):
        # test
        result = collectionToMatrixDict(User)
        # expect
        expected = dict()
        expected[1] = 0
        expected[3] = 1
        expected[4] = 2
        expected[99] = 3
        self.assertEqual(expected, result)

    def test_matrix_to_collectionDict(self):
        # test
        result = matrixToCollectionDict(User)
        # expect
        expected = dict()
        expected[0] = User.objects.get(id=1)
        expected[1] = User.objects.get(id=3)
        expected[2] = User.objects.get(id=4)
        expected[3] = User.objects.get(id=99)
        self.assertEqual(expected, result)

    def test_prepareMyPredictions_LastUser(self):
        # prepare
        user = User.objects.get(id=99)
        # test
        result = prepareMyPredictions(self._params, user)
        # expect
        expected = np.array([[1], [2], [3], [4], [5]])
        self.assertEqual(expected.all(), result.all())

    def test_printTopList(self):
        # prepare
        user = User.objects.get(id=99)
        ratings = list()
        ratings.append((4, 5))
        ratings.append((3, 4))
        ratings.append((2, -3))
        ratings.append((1, 2))
        ratings.append((0, 1))
        Y = np.array([[1, 1, 1, 0], [2, 2, 2, 0], [3, 3, 3, 0], [4, 4, 4, 4], [5, 5, 5, 0]])
        # test
        result = printTopList(Y, user, ratings)
        # expect
        expectedList = list()
        expectedList.append((5, Film.objects.get(Title="film5")))
        expectedList.append((2, Film.objects.get(Title="film2")))
        expectedList.append((1, Film.objects.get(Title="film1")))
        self.assertEqual(expectedList, result)
