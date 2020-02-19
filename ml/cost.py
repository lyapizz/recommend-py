import numpy as np

def cofiCostFunc(X, Theta, Y, R, num_users, num_movies, num_features, lambda_reg):
    # COFICOSTFUNC Collaborative filtering cost function
    # [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, num_features, lambda )
    # returns the cost and gradient for the collaborative filtering problem.

    print('X = ', X,'\nTheta = ',Theta,'\nY = ', Y,'\nR = ', R,'\nnum_users = ', num_users,'\nnum_movies = ', num_movies,'\nnum_features = ', num_features,'\nlambda_reg = ', lambda_reg)

    X_grad = np.zeros(np.shape(X))
    Theta_grad = np.zeros(np.shape(Theta))

    errMatrix = np.dot(X, Theta.T) *R - Y
    J = (errMatrix * errMatrix).sum()/2

    grad = (X_grad[:], Theta_grad[:])

    return (J, grad)