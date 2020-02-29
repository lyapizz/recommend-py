import time

import numpy as np
import scipy as scipy
from scipy.io import loadmat
from scipy.optimize import minimize

from ml.checkCostFunction import checkCostFunction
from ml.cost import cofiCostFuncCost, cofiCostFuncGrad
from ml.loadMovieList import loadMovieList
from ml.normalizeRatings import normalizeRatings

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
J = cofiCostFuncCost(params, Y, R, num_users, num_movies, num_features, 0)

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
J = cofiCostFuncCost(params, Y, R, num_users, num_movies, num_features, 1.5)

print('Cost at loaded parameters (lambda = 1.5): ', J, '\n(this value should be about 31.34)\n')

# ======= Part 5: Collaborative Filtering Gradient Regularization ======
#  Once your cost matches up with ours, you should proceed to implement
#  regularization for the gradient.
#

print('\nChecking Gradients (with regularization) ... \n')

#  Check gradients by running checkNNGradients
checkCostFunction(lambda_reg=1.5)

## ============== Part 6: Entering ratings for a new user ===============
#  Before we will train the collaborative filtering model, we will first
#  add ratings that correspond to a new user that we just observed. This
#  part of the code will also allow you to put in your own ratings for the
#  movies in our dataset!
#
movieList = loadMovieList()

#  Initialize my ratings
my_ratings = np.zeros(len(movieList))

# Check the file movie_idx.txt for id of each movie in our dataset
# For example, Toy Story (1995) has ID 1, so to rate it "4", you can set
my_ratings[1-1] = 4

# Or suppose did not enjoy Silence of the Lambs (1991), you can set
my_ratings[98-1] = 2

# We have selected a few movies we liked / did not like and the ratings we
# gave are as follows:
my_ratings[7-1] = 3
my_ratings[12-1] = 5
my_ratings[54-1] = 4
my_ratings[64-1] = 5
my_ratings[66-1] = 3
my_ratings[69-1] = 5
my_ratings[183-1] = 4
my_ratings[226-1] = 5
my_ratings[355-1] = 5

# print('\n\nNew user ratings:\n')
# for i in range(len(my_ratings)):
#     if my_ratings[i] != 0:
#         print('Rated ', my_ratings[i], ' for ', movieList[i+1])

## ================== Part 7: Learning Movie Ratings ====================
#  Now, you will train the collaborative filtering model on a movie rating 
#  dataset of 1682 movies and 943 users
#

print('\nTraining collaborative filtering...\n')

#  Load data
mat_contents = loadmat('ml/resources/ex8_movies.mat')
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
num_features = 10 #set 10
#Y = np.array([[5, 5, 1, 1], [5, 0, 0, 1], [0, 4, 1, 0], [1, 1, 5, 4], [1, 1, 5, 0]])
#R = np.array([[1, 1, 1, 1], [1, 0, 0, 1], [0, 1, 1, 0], [1, 1, 1, 1], [1, 1, 1, 0]])

# #  Normalize Ratings
(Ynorm, Ymean) = normalizeRatings(Y, R)
# print('Ymean=', Ymean)
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
res1 = scipy.optimize.fmin_cg(cofiCostFuncCost, initial_parameters, fprime=cofiCostFuncGrad, args=(Ynorm, R, num_users, num_movies, num_features, lambda_reg))
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

## ================== Part 8: Recommendation for you ====================
#  After training the model, you can now make recommendations by computing
#  the predictions matrix.
#

p = np.dot(X, Theta.T)
userId = 0
my_predictions = p[:, userId] + Ymean[:, 0]

movieList = loadMovieList()
print('\nTop recommendations for you:\n')
r = sorted(enumerate(my_predictions),key=lambda x: x[1], reverse=True)
count = 25
for item in r:
        print('Predicting rating %.1f for movie %s' % (item[1], movieList[item[0] + 1]))
        count = count - 1
        if count == 0:
            break


print('\n\nOriginal ratings provided:\n')
for i in range(len(my_ratings)):
    if my_ratings[i] != 0:
        print('Rated %.1f (pred. %.1f) for %s' % (my_ratings[i], my_predictions[i], movieList[i+1]))

print('\nCompare for 1 user:\n')
userId = 1
my_predictions = p[:, userId] + Ymean[:, 0]
for i in range(num_movies):
    if Y[i][userId] != 0:
        print('Rated %.1f (pred. %.1f) for %s' % (Y[i][userId], my_predictions[i], movieList[i + 1]))

print('Success!')
