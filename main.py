import scipy.io as sio
import numpy as np

from scipy.io import loadmat

from ml.checkCostFunction import checkCostFunction
from ml.cost import cofiCostFunc

print('Loading movie ratings dataset.\n')
mat_contents = loadmat('ml/resources/ex8_movies.mat')
#  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies on
#  943 users
#
#  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
#  rating to movie i

#  From the matrix, we can compute statistics like average rating.

(Y, R) = (mat_contents.get("Y"), mat_contents.get("R"))
print('Average rating for movie 1 (Toy Story): ', np.mean(Y[0][R[0, :]]), '/ 5 \n')

# input('Program paused. Press enter to continue.')
# ============ Part 2: Collaborative Filtering Cost Function ===========
#  You will now implement the cost function for collaborative filtering.
#  To help you debug your cost function, we have included set of weights
#  that we trained on that. Specifically, you should complete the code in
#  cofiCostFunc.m to return J.

#  Load pre-trained weights (X, Theta, num_users, num_movies, num_features)
mat_params = loadmat('ml/resources/ex8_movieParams.mat')
#  Reduce the data set size so that this runs faster
num_users = 4
num_movies = 5
num_features = 3

X = mat_params.get('X')[0:num_movies, 0:num_features]
Theta = mat_params.get('Theta')[0:num_users, 0:num_features]

Y = Y[0:num_movies, 0:num_users]
R = R[0:num_movies, 0:num_users]

# shape matrix to vector for quick calculations
params = np.concatenate((X.flatten(), Theta.flatten()))
# Evaluate cost function
J, grad = cofiCostFunc(params, Y, R, num_users, num_movies, num_features, 0)

print('[Cost at loaded parameters: ', J, '(this value should be about 22.22)]')

# ============== Part 3: Collaborative Filtering Gradient ==============
#  Once your cost function matches up with ours, you should now implement
#  the collaborative filtering gradient function. Specifically, you should
#  complete the code in cofiCostFunc.m to return the grad argument.
#
print('\nChecking Gradients (without regularization) ... \n')

#  Check gradients by running checkNNGradients
checkCostFunction()

# ========= Part 4: Collaborative Filtering Cost Regularization ========
#  Now, you should implement regularization for the cost function for
#  collaborative filtering. You can implement it by adding the cost of
#  regularization to the original cost computation.
#

#  Evaluate cost function
J, grad = cofiCostFunc(params, Y, R, num_users, num_movies, num_features, 1.5)

print('Cost at loaded parameters (lambda = 1.5): ', J,'\n(this value should be about 31.34)\n')

input("")


