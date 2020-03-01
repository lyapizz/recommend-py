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


def train(my_ratings):
    print('\nTraining collaborative filtering...\n')
    #  Load data
    mat_contents = loadmat('ml/test/resources/ex8_movies.mat')
    (Y, R) = (mat_contents.get("Y"), mat_contents.get("R"))
    #  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies by
    #  943 users
    #
    #  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
    #  rating to movie i
    #  Add our own ratings to the data matrix
    Y = np.column_stack((my_ratings, Y))
    R = np.column_stack((my_ratings != 0, R))
    # Test example from exercies
    num_features = 10
    # Y = np.array([[5, 5, 1, 1], [5, 0, 0, 1], [0, 4, 1, 0], [1, 1, 5, 4], [1, 1, 5, 0]])
    # R = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0]])
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
    lambda_reg = 10
    start_time = time.time()
    res1 = scipy.optimize.fmin_cg(cofiCostFuncCost, initial_parameters, fprime=cofiCostFuncGrad,
                                  args=(Ynorm, R, num_users, num_movies, num_features, lambda_reg))
    print("--- %s seconds ---" % (time.time() - start_time))
    # print ('res1 = ', res1)
    # theta = minimize(cofiCostFuncSingle, initial_parameters,
    #                 args=(Ynorm, R, num_users, num_movies, num_features, lambda_reg), method='Nelder-Mead')
    # theta = theta.x
    #
    # Unfold the returned theta back into X and Theta
    X = np.reshape(res1[0:num_movies * num_features], (num_movies, num_features))
    Theta = np.reshape(res1[num_movies * num_features:], (num_users, num_features))
    print('Recommender system learning completed.\n')
    print('\nProgram paused. Press enter to continue.\n')

    return {'X': X, 'Theta': Theta, 'Y' : Y, 'Ymean' : Ymean}