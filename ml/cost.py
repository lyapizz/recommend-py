import numpy as np

def cofiCostFuncCost(params, Y, R, num_users, num_movies, num_features, lambda_reg):
    # Unfold the X and Theta matrices from params
    X = params[0:num_movies * num_features].reshape(num_movies, num_features)
    Theta = params[num_movies * num_features:].reshape(num_users, num_features)

    # calculate difference between actual and expected rating of film
    errMatrix = np.dot(X, Theta.T) * R - Y
    J = (errMatrix * errMatrix).sum() / 2

    # add regularization summands
    theta_reg = lambda_reg / 2 * np.sum(Theta * Theta)
    x_reg = lambda_reg / 2 * np.sum(X * X)
    J = J + theta_reg + x_reg
    return J

def cofiCostFuncGrad(params, Y, R, num_users, num_movies, num_features, lambda_reg):
    # Unfold the X and Theta matrices from params
    X = params[0:num_movies * num_features].reshape(num_movies, num_features)
    Theta = params[num_movies * num_features:].reshape(num_users, num_features)

    # calculate difference between actual and expected rating of film
    errMatrix = np.dot(X, Theta.T) * R - Y

    # calculate gradients
    X_grad = np.dot(errMatrix, Theta) + lambda_reg * X
    Theta_grad = np.dot(errMatrix.T, X) + lambda_reg * Theta

    grad = np.concatenate((X_grad.flatten(), Theta_grad.flatten()))

    return grad

def cofiCostFunc(params, Y, R, num_users, num_movies, num_features, lambda_reg):
    # COFICOSTFUNC Collaborative filtering cost function
    # [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, num_features, lambda )
    # returns the cost and gradient for the collaborative filtering problem.

    # Unfold the X and Theta matrices from params
    X = params[0:num_movies * num_features].reshape(num_movies, num_features)
    Theta = params[num_movies * num_features:].reshape(num_users, num_features)

    #print('X = ', X, '\nTheta = ', Theta, '\nY = ', Y, '\nR = ', R, '\nnum_users = ', num_users, '\nnum_movies = ',
    #      num_movies, '\nnum_features = ', num_features, '\nlambda_reg = ', lambda_reg)

    # calculate difference between actual and expected rating of film
    errMatrix = np.dot(X, Theta.T) * R - Y
    J = (errMatrix * errMatrix).sum() / 2

    # add regularization summands
    theta_reg = lambda_reg/2 * np.sum(Theta*Theta)
    x_reg = lambda_reg/2 * np.sum(X*X)
    J = J + theta_reg + x_reg

    # calculate gradients
    X_grad = np.dot(errMatrix, Theta) + lambda_reg*X
    Theta_grad = np.dot(errMatrix.T, X) + lambda_reg*Theta

    grad = np.concatenate((X_grad.flatten(), Theta_grad.flatten()))

    return J, grad

