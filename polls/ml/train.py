import time

import numpy as np
import scipy as scipy
from django.conf import settings
from scipy.optimize import minimize

from ..ml.cost import cofiCostFuncCost, cofiCostFuncGrad
from ..ml.normalizeRatings import normalizeRatings
from ..ml.util import filterFilmsWithoutReview


def train(Y, R):
    R = filterFilmsWithoutReview(Y, R, settings.MIN_REVIEWS)
    print('\nTraining collaborative filtering...\n')

    # #  Normalize Ratings
    (Ynorm, Ymean) = normalizeRatings(Y, R)
    #
    #  Useful Values
    num_users = Y.shape[1]
    num_movies = Y.shape[0]
    #
    # Set Initial Parameters (Theta, X)
    X = np.random.rand(num_movies, settings.NUMBER_OF_FEATURES)
    Theta = np.random.rand(num_users, settings.NUMBER_OF_FEATURES)
    #
    initial_parameters = np.concatenate((X.flatten(), Theta.flatten()))
    #
    # # Set Regularization
    start_time = time.time()
    localMinimum = scipy.optimize.fmin_cg(cofiCostFuncCost, initial_parameters, fprime=cofiCostFuncGrad,
                                          args=(Ynorm, R, num_users, num_movies, settings.NUMBER_OF_FEATURES,
                                                settings.LAMBDA_REG), maxiter=settings.MAX_ITERATIONS)
    print("--- %s seconds ---" % (time.time() - start_time))

    # Unfold the returned theta back into X and Theta
    X = np.reshape(localMinimum[0:num_movies * settings.NUMBER_OF_FEATURES], (num_movies, settings.NUMBER_OF_FEATURES))
    Theta = np.reshape(localMinimum[num_movies * settings.NUMBER_OF_FEATURES:],
                       (num_users, settings.NUMBER_OF_FEATURES))
    print('Recommender system learning completed.\n')

    J = cofiCostFuncCost(np.concatenate((X.flatten(), Theta.flatten())), Ynorm, R, num_users, num_movies,
                         settings.NUMBER_OF_FEATURES, settings.LAMBDA_REG)
    return {'X': X, 'Theta': Theta, 'Y': Y, 'Ymean': Ymean, 'localMinimum': localMinimum, 'J': J}
