import numpy as np

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

    theta_reg = calcRegulatizationSummand(Theta, lambda_reg)
    x_reg = calcRegulatizationSummand(X, lambda_reg)
    J = J + theta_reg + x_reg

    # calculate gradients
    X_grad = np.dot(errMatrix, Theta)
    Theta_grad = np.dot(errMatrix.T, X)

    grad = np.concatenate((X_grad.flatten(), Theta_grad.flatten()))
    return J, grad

# calculate regulatization summand for Theta and X
def calcRegulatizationSummand(matrix, lambda_reg):
    reg = 0
    for j in range(matrix.shape[0]):
        for k in range(matrix.shape[1]):
            reg = reg + matrix[j][k] * matrix[j][k]
    return lambda_reg * reg / 2