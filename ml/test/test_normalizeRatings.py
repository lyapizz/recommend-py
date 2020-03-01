from unittest import TestCase

import numpy as np
from ml.normalizeRatings import normalizeRatings

class Test(TestCase):

    def test_NormalizeRatings(self):
        # Evaluate cost function
        Y = np.array([[5, 5, 0, 0], [5, 0, 0, 0], [0, 4, 0, 0], [0, 0, 5, 4], [0, 0, 5, 0]])
        R = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0]])
        (Ynorm, Ymean) = normalizeRatings(Y, R)

        expectedYmean = np.array([[2.5], [2.5], [2], [2.25], [1.6666666666666667]])
        expectedYnorm = np.array([
            [2.5                , 2.5                , -2.5             , -2.5],
            [2.5                , 0                  , 0                , -2.5],
            [0                  , 2                  , -2               , 0],
            [-2.25              , -2.25              , 2.75             , 1.75],
            [-1.6666666666666667, -1.6666666666666667, 3.333333333333333, 0]])
        self.assertTrue((expectedYmean == Ymean).all())
        self.assertTrue((expectedYnorm == Ynorm).all())