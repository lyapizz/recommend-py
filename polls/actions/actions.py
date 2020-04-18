import numpy as np

from .films.load_films import loadFilmsMap


# This method return top recommendations for exact user
# using already trained model
def printTopRecommendations(params, user):
    X = params.get('X')
    Theta = params.get('Theta')
    Y = params.get('Y')
    Ymean = params.get('Ymean')
    # num_movies = Y.shape[0]

    p = np.dot(X, Theta.T)

    my_predictions = p[:, user.id - 1] + Ymean[:, 0]
    movieList = loadFilmsMap()
    print('\nTop recommendations for %s :\n' % user.username)
    r = sorted(enumerate(my_predictions), key=lambda x: x[1], reverse=True)

    topList = list()
    count = 10
    for item in r:
        if item[1] < 0:
            continue
        movie = movieList[item[0] + 1]
        s = 'Predicting rating %.1f for movie %s (%s)' % (item[1], movie.Title, movie.Year)
        topList.append(s)
        print(s)
        count = count - 1
        if count == 0:
            break
    return topList
    # print('\n\nOriginal ratings provided:\n')
    # for i in range(len(my_ratings)):
    #     if my_ratings[i] != 0:
    #         print('Rated %.1f (pred. %.1f) for %s' % (my_ratings[i], my_predictions[i], movieList[i + 1]))

    # print('\nCompare for 0 user:\n')
    # my_predictions = p[:, userId] + Ymean[:, 0]
    # for i in range(num_movies):
    #    if Y[i][userId] != 0:
    #        print('Rated %.1f (pred. %.1f) for %s' % (Y[i][userId], my_predictions[i], movieList[i + 1]))
