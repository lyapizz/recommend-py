import scipy.io as sio
import numpy as np

print('Loading movie ratings dataset.\n')
mat_contents = sio.loadmat('ml/resources/ex8_movies.mat')
#  Y is a 1682x943 matrix, containing ratings (1-5) of 1682 movies on
#  943 users
#
#  R is a 1682x943 matrix, where R(i,j) = 1 if and only if user j gave a
#  rating to movie i

#  From the matrix, we can compute statistics like average rating.
Y = mat_contents.get('Y')
R = mat_contents.get('R')
print('Average rating for movie 1 (Toy Story): ', np.mean(Y[0][R[0, :]]),  '/ 5 \n')