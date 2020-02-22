import numpy as np

def cofiCostFunc(X, Theta, Y, R, num_users, num_movies, num_features, lambda_reg):
    # COFICOSTFUNC Collaborative filtering cost function
    # [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, num_features, lambda )
    # returns the cost and gradient for the collaborative filtering problem.

    print('X = ', X,'\nTheta = ',Theta,'\nY = ', Y,'\nR = ', R,'\nnum_users = ', num_users,'\nnum_movies = ', num_movies,'\nnum_features = ', num_features,'\nlambda_reg = ', lambda_reg)

    X_grad = np.zeros(np.shape(X))
    Theta_grad = np.zeros(np.shape(Theta))
    # calculate difference between actual and expected rating of film
    errMatrix = np.dot(X, Theta.T) *R - Y
    J = (errMatrix * errMatrix).sum()/2

    for i in range(num_movies):
        for k in range(num_features):
            sum = 0
            for j in range(num_users):
                if R[i][j] == 1:
                    sum = sum + (np.dot(Theta[j], X[i]) - Y[i][j]) * Theta[j][k]
            X_grad[i, k] = sum

    for j in range(num_users):
        for k in range(num_features):
            sum = 0
            for i in range(num_movies):
                if R[i][j] == 1:
                    sum = sum + (np.dot(Theta[j], X[i]) - Y[i][j]) * X[i][k]
            Theta_grad[j, k] = sum




    grad = (X_grad[:], Theta_grad[:])

    return (J, grad)