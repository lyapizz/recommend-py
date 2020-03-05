from unittest import TestCase

import numpy as np

from ml.util import filterFilmsWithoutReview


class Test(TestCase):
    def test_no_enougn_reviews(self):
        #when
        Y = np.array([[5, 5, 0, 0]])
        R = np.array([[1, 1, 0, 0]])
        #test
        R = filterFilmsWithoutReview(Y, R, 3)
        #then
        expectedR = np.array([[0, 0, 0, 0]])
        self.assertTrue((expectedR == R).all())

    def test_no_filter(self):
        Y = np.array([[5, 5, 0, 0]])
        R = np.array([[1, 1, 0, 0]])

        R = filterFilmsWithoutReview(Y, R, 2)

        expectedR = np.array([1, 1, 0, 0])
        self.assertTrue((expectedR == R).all())

    def test_two_films(self):
        Y = np.array([[5, 5, 0, 0], [0, 3, 0, 0]])
        R = np.array([[1, 1, 0, 0], [0, 1, 0, 0]])

        R = filterFilmsWithoutReview(Y, R, 2)

        expectedR = np.array([[1, 1, 0, 0], [0, 0, 0, 0]])
        self.assertTrue((expectedR == R).all())
