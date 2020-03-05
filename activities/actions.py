import numpy as np

from ml.test.loadMovieList import loadMovieList


## ============== Part 6: Entering ratings for a new user ===============
#  Before we will train the collaborative filtering model, we will first
#  add ratings that correspond to a new user that we just observed. This
#  part of the code will also allow you to put in your own ratings for the
#  movies in our dataset!
#
def addNewRecommendations():
    movieList = loadMovieList()
    #  Initialize my ratings
    my_ratings = np.zeros(len(movieList))
    # Check the file movie_idx.txt for id of each movie in our dataset
    # For example, Toy Story (1995) has ID 1, so to rate it "4", you can set
    my_ratings[1 - 1] = 4
    # Or suppose did not enjoy Silence of the Lambs (1991), you can set
    my_ratings[98 - 1] = 2
    # We have selected a few movies we liked / did not like and the ratings we
    # gave are as follows:
    my_ratings[7 - 1] = 3
    my_ratings[12 - 1] = 5
    my_ratings[54 - 1] = 4
    my_ratings[64 - 1] = 5
    my_ratings[66 - 1] = 3
    my_ratings[69 - 1] = 5
    my_ratings[183 - 1] = 4
    my_ratings[226 - 1] = 5
    my_ratings[355 - 1] = 5
    return my_ratings

def printTopRecommendations(params):
    X = params.get('X')
    Theta = params.get('Theta')
    Y = params.get('Y')
    Ymean = params.get('Ymean')
    num_movies = Y.shape[0]

    p = np.dot(X, Theta.T)
    userId = 0
    my_predictions = p[:, userId] + Ymean[:, 0]
    movieList = loadMovieList()
    print('\nTop recommendations for you:\n')
    r = sorted(enumerate(my_predictions), key=lambda x: x[1], reverse=True)
    count = 25
    for item in r:
        print('Predicting rating %.1f for movie %s' % (item[1], movieList[item[0] + 1]))
        count = count - 1
        if count == 0:
            break

    # print('\n\nOriginal ratings provided:\n')
    # for i in range(len(my_ratings)):
    #     if my_ratings[i] != 0:
    #         print('Rated %.1f (pred. %.1f) for %s' % (my_ratings[i], my_predictions[i], movieList[i + 1]))

    print('\nCompare for 0 user:\n')
    my_predictions = p[:, userId] + Ymean[:, 0]
    for i in range(num_movies):
        if Y[i][userId] != 0:
            print('Rated %.1f (pred. %.1f) for %s' % (Y[i][userId], my_predictions[i], movieList[i + 1]))