from random import randint

import numpy as np
from django.test import SimpleTestCase, override_settings

from polls.ml.train import train


@override_settings(NUMBER_OF_FEATURES=2)
class Test(SimpleTestCase):

    def test_train_ideal_film(self):
        # prepare
        Y = np.zeros((1, 100))
        for i in range(1, 100):
            Y[0][i] = 5

        R = np.zeros(Y.shape)
        R[Y > 0] = 1
        # do
        result = train(Y=Y, R=R)
        # check
        X = result.get('X')
        Theta = result.get('Theta')
        Ymean = result.get('Ymean')

        p = np.dot(X, Theta.T)
        userId = 0
        my_predictions = p[:, userId] + Ymean[:, 0]
        print(my_predictions)
        self.assertTrue(abs(my_predictions[0] - 5.) < 1e4)

    def test_train_two_films(self):
        # prepare
        Y = np.zeros((2, 100))
        for i in range(1, 100):
            Y[0][i] = 5
            Y[1][i] = 1

        R = np.zeros(Y.shape)
        R[Y > 0] = 1
        # do
        result = train(Y=Y, R=R)
        # check
        X = result.get('X')
        Theta = result.get('Theta')
        Ymean = result.get('Ymean')

        p = np.dot(X, Theta.T)
        userId = 0
        my_predictions = p[:, userId] + Ymean[:, 0]
        print(my_predictions)
        self.assertTrue(abs(my_predictions[0] - 5.) < 1e4)
        self.assertTrue(abs(my_predictions[1] - 1.) < 1e4)

    def test_train_pretty_good_film(self):
        # prepare
        Y = np.zeros((1, 100))
        for i in range(1, 100):
            Y[0][i] = randint(4, 5)

        R = np.zeros(Y.shape)
        R[Y > 0] = 1
        # do
        result = train(Y=Y, R=R)
        # check
        X = result.get('X')
        Theta = result.get('Theta')
        Ymean = result.get('Ymean')

        p = np.dot(X, Theta.T)
        userId = 0
        my_predictions = p[:, userId] + Ymean[:, 0]
        print(my_predictions)
        self.assertTrue(my_predictions[0] >= 4.)
        self.assertTrue(my_predictions[0] <= 5.)
