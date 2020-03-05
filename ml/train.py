import time

import numpy as np
import scipy as scipy

from scipy.io import loadmat
from scipy.optimize import minimize

## ================== Part 7: Learning Movie Ratings ====================
#  Now, you will train the collaborative filtering model on a movie rating
#  dataset of 1682 movies and 943 users
#
from ml.cost import cofiCostFuncCost, cofiCostFuncGrad
from ml.normalizeRatings import normalizeRatings
from ml.util import filterFilmsWithoutReview


def train(num_features, **kwargs):
    # todo calculate R at the end
    if 'Y' in kwargs and 'R' in kwargs:
        Y = kwargs.get('Y')
        R = kwargs.get('R')
    else:
        mat_contents = loadmat('ml/test/resources/ex8_movies.mat')
        (Y, R) = (mat_contents.get("Y"), mat_contents.get("R"))
    #  Add our own ratings to the data matrix
    if 'my_ratings' in kwargs:
        my_ratings = kwargs.get('my_ratings')
        Y = np.column_stack((my_ratings, Y))
        R = np.column_stack((my_ratings != 0, R))

    lambda_reg = kwargs.get('lambda_reg', 10)
    maxiter = kwargs.get('maxiter', 10)

    minimumReviewsCount= kwargs.get('minimumReviewsCount', 5)
    R = filterFilmsWithoutReview(Y, R, minimumReviewsCount)

    print('\nTraining collaborative filtering...\n')
    #  Load data

    # #  Normalize Ratings
    (Ynorm, Ymean) = normalizeRatings(Y, R)
    #
    #  Useful Values
    num_users = Y.shape[1]
    num_movies = Y.shape[0]
    #
    # Set Initial Parameters (Theta, X)
    X = np.random.rand(num_movies, num_features)
    Theta = np.random.rand(num_users, num_features)
    #
    initial_parameters = np.concatenate((X.flatten(), Theta.flatten()))
    #
    # # Set Regularization
    start_time = time.time()
    localMinimum = scipy.optimize.fmin_cg(cofiCostFuncCost, initial_parameters, fprime=cofiCostFuncGrad,
                                          args=(Ynorm, R, num_users, num_movies, num_features, lambda_reg), maxiter=maxiter)
    print("--- %s seconds ---" % (time.time() - start_time))
    # print ('localMinimum = ', localMinimum)
    # theta = minimize(cofiCostFuncSingle, initial_parameters,
    #                 args=(Ynorm, R, num_users, num_movies, num_features, lambda_reg), method='Nelder-Mead')
    # theta = theta.x
    #
    # Unfold the returned theta back into X and Theta
    X = np.reshape(localMinimum[0:num_movies * num_features], (num_movies, num_features))
    Theta = np.reshape(localMinimum[num_movies * num_features:], (num_users, num_features))
    print('Recommender system learning completed.\n')

    J = cofiCostFuncCost(np.concatenate((X.flatten(), Theta.flatten())), Ynorm, R, num_users, num_movies, num_features, lambda_reg)

    return {'X': X, 'Theta': Theta, 'Y': Y, 'Ymean': Ymean, 'localMinimum': localMinimum, 'J' : J}