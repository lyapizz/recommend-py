import numpy as np

def cofiCostFunc(X, Theta, Y, R, num_users, num_movies, num_features, lambda_reg):
    # COFICOSTFUNC Collaborative filtering cost function
    # [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, num_features, lambda )
    # returns the cost and gradient for the collaborative filtering problem.

    print('Start cost Func evaluation:')
    print('X = ', X,'\nTheta = ',Theta,'\nY = ', Y,'\nR = ', R,'\nnum_users = ', num_users,'\nnum_movies = ', num_movies,'\nnum_features = ', num_features,'\nlambda_reg = ', lambda_reg)

    J = 0
    X_grad = np.zeros(np.shape(X))
    Theta_grad = np.zeros(np.shape(Theta))

    grad = (X_grad[:], Theta_grad[:])

    print('Success!')
    return (J, grad)