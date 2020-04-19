import numpy as np
from django.test import TestCase
from django_registration.forms import User

from polls.actions.actions import collectionToMatrixDict, matrixToCollectionDict, prepareMyPredictions


class Test(TestCase):

    def setUp(cls):
        cls._num_users = 4
        cls._num_movies = 5
        cls._num_features = 1

        cls._params = dict()
        cls._params['X'] = np.array([[1], [1], [1], [1], [1]])
        cls._params['Theta'] = np.array([[1], [1], [1], [1]])
        cls._params['Ymean'] = np.array([[1], [2], [3], [4], [5]])

        User.objects.create(id=1, username='user1')
        User.objects.create(id=3, username='user2')
        User.objects.create(id=4, username='user3')
        User.objects.create(id=5, username='user4')

    def test_collection_to_matrix_dict(self):
        # test
        result = collectionToMatrixDict(User)
        # expect
        expected = dict()
        expected[1] = 0
        expected[3] = 1
        expected[4] = 2
        expected[5] = 3
        self.assertEqual(expected, result)

    def test_matrix_to_collectionDict(self):
        # test
        result = matrixToCollectionDict(User)
        # expect
        expected = dict()
        expected[0] = User.objects.get(id=1)
        expected[1] = User.objects.get(id=3)
        expected[2] = User.objects.get(id=4)
        expected[3] = User.objects.get(id=5)
        self.assertEqual(expected, result)

    def test_prepareMyPredictions_LastUser(self):
        # prepare
        user = User.objects.get(id=5)
        # test
        result = prepareMyPredictions(self._params, user)
        # expect
        expected = dict()
        expected[0] = User.objects.get(id=1)
        expected[1] = User.objects.get(id=3)
        expected[2] = User.objects.get(id=4)
        self.assertEqual(expected, result)
