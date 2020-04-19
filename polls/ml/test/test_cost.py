import os
from unittest import TestCase

import numpy as np
from scipy.io import loadmat

from ...ml.cost import cofiCostFuncCost
from ...ml.test.checkCostFunction import checkCostFunction


class Test(TestCase):

    @classmethod
    def setUpClass(cls):
        my_dir = os.path.dirname(__file__)
        mat_contents = loadmat(os.path.join(my_dir, 'resources/ex8_movies.mat'))
        #  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies on
        #  943 users
        #
        #  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
        #  rating to movie i

        #  From the matrix, we can compute statistics like average rating.

        (cls._Y, cls._R) = (mat_contents.get("Y"), mat_contents.get("R"))
        mat_params = loadmat(os.path.join(my_dir, 'resources/ex8_movieParams.mat'))
        #  Reduce the data set size so that this runs faster
        cls._num_users = 4
        cls._num_movies = 5
        cls._num_features = 3

        cls._X = mat_params.get('X')[0:cls._num_movies, 0:cls._num_features]
        cls._Theta = mat_params.get('Theta')[0:cls._num_users, 0:cls._num_features]

        cls._Y = cls._Y[0:cls._num_movies, 0:cls._num_users]
        cls._R = cls._R[0:cls._num_movies, 0:cls._num_users]

        # shape matrix to vector for quick calculations
        cls._params = np.concatenate((cls._X.flatten(), cls._Theta.flatten()))

    def test_cost(self):
        # Evaluate cost function
        J = cofiCostFuncCost(self._params, self._Y, self._R, self._num_users, self._num_movies, self._num_features, 0)
        self.assertEqual(22.22, round(J, 2), msg='Cost at loaded parameters should be about 22.22')

    def test_cost_reg(self):
        # Evaluate cost function
        J = cofiCostFuncCost(self._params, self._Y, self._R, self._num_users, self._num_movies, self._num_features, 1.5)
        self.assertEqual(31.34, round(J, 2), msg='Cost at loaded parameters (lambda = 1.5): should be about 31.34)')

    def test_checkGradient(self):
        diff = checkCostFunction()
        self.assertTrue(diff < 1e-9, msg='If your cost function implementation is correct, then \n'
                                                 'the relative difference will be small (less than 1e-9). \n')
    def test_checkGradient_reg(self):
        diff = checkCostFunction(lambda_reg=1.5)
        self.assertTrue(diff < 1e-9, msg='If your cost function implementation is correct, then \n'
                                                 'the relative difference will be small (less than 1e-9). \n')