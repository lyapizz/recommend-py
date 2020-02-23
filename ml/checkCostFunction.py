import numpy as np
import scipy as scipy

from ml.computeNumericalGradient import computeNumericalGradient
from ml.cost import cofiCostFunc


def checkCostFunction(**kwargs):
    lambda_reg = kwargs.get('lambda_reg', 0)
    # Create small problem
    X_t = scipy.rand(4, 3)
    Theta_t = scipy.rand(5, 3)
    # Zap out most entries
    Y = np.dot(X_t, Theta_t.T)
    Y[scipy.rand(*Y.shape) > 0.5] = 0

    R = np.zeros(Y.shape)
    R[Y > 0] = 1
    # Run Gradient Checking
    X = scipy.rand(*X_t.shape)
    Theta = scipy.rand(*Theta_t.shape)

    num_users = Y.shape[1]
    num_movies = Y.shape[0]
    num_features = Theta_t.shape[1]

    params = np.concatenate((X.flatten(), Theta.flatten()))

    numgrad = computeNumericalGradient(cofiCostFunc, params, Y, R, num_users, num_movies, num_features, lambda_reg)

    (cost, grad) = cofiCostFunc(params, Y, R, num_users, num_movies, num_features, lambda_reg)

    diff = np.linalg.norm(numgrad - grad) / np.linalg.norm(numgrad + grad)
    print('[If your cost function implementation is correct, then \n'
            'the relative difference will be small (less than 1e-9). \n'
            '\nRelative Difference: ', diff, ']')
