import numpy as np
from numpy.random import rand

from polls.ml.computeNumericalGradient import computeNumericalGradient
from polls.ml.cost import cofiCostFuncGrad, cofiCostFuncCost


def checkCostFunction(**kwargs):
    lambda_reg = kwargs.get('lambda_reg', 0)
    # Create small problem
    X_t = rand(4, 3)
    Theta_t = rand(5, 3)
    # Zap out most entries
    Y = np.dot(X_t, Theta_t.T)
    Y[rand(*Y.shape) > 0.5] = 0

    R = np.zeros(Y.shape)
    R[Y > 0] = 1
    # Run Gradient Checking
    X = rand(*X_t.shape)
    Theta = rand(*Theta_t.shape)

    num_users = Y.shape[1]
    num_movies = Y.shape[0]
    num_features = Theta_t.shape[1]

    params = np.concatenate((X.flatten(), Theta.flatten()))

    numgrad = computeNumericalGradient(cofiCostFuncCost, params, Y, R, num_users, num_movies, num_features, lambda_reg)

    grad = cofiCostFuncGrad(params, Y, R, num_users, num_movies, num_features, lambda_reg)

    diff = np.linalg.norm(numgrad - grad) / np.linalg.norm(numgrad + grad)
    return diff

