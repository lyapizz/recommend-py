import numpy as np

from db.films.load_films import loadFilmsMap


## ============== Part 6: Entering ratings for a new user ===============
#  Before we will train the collaborative filtering model, we will first
#  add ratings that correspond to a new user that we just observed. This
#  part of the code will also allow you to put in your own ratings for the
#  movies in our dataset!
#
from db.users.actions import get_user_by_name

def printTopRecommendations(params, name):
    X = params.get('X')
    Theta = params.get('Theta')
    Y = params.get('Y')
    Ymean = params.get('Ymean')
    num_movies = Y.shape[0]

    p = np.dot(X, Theta.T)
    #todo this row may be refactore
    userId = get_user_by_name(name)["user_ID"]

    my_predictions = p[:, userId] + Ymean[:, 0]
    movieList = loadFilmsMap()
    print('\nTop recommendations for %s :\n' % name)
    r = sorted(enumerate(my_predictions), key=lambda x: x[1], reverse=True)
    count = 10
    for item in r:
        print('Predicting rating %.1f for movie %s' % (item[1], movieList[item[0] + 1]["Title"]))
        count = count - 1
        if count == 0:
            break

    # print('\n\nOriginal ratings provided:\n')
    # for i in range(len(my_ratings)):
    #     if my_ratings[i] != 0:
    #         print('Rated %.1f (pred. %.1f) for %s' % (my_ratings[i], my_predictions[i], movieList[i + 1]))

    # print('\nCompare for 0 user:\n')
    # my_predictions = p[:, userId] + Ymean[:, 0]
    # for i in range(num_movies):
    #    if Y[i][userId] != 0:
    #        print('Rated %.1f (pred. %.1f) for %s' % (Y[i][userId], my_predictions[i], movieList[i + 1]))