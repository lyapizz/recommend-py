import numpy as np
from django_registration.forms import User

# This method return top recommendations for exact user
# using already trained model
from ..models import Film


def printTopRecommendations(params, user):
    print('\nTop recommendations for %s :\n' % user.username)

    my_predictions = prepareMyPredictions(params, user)
    ratings = sorted(enumerate(my_predictions), key=lambda x: x[1], reverse=True)

    return printTopList(params, user, ratings)


def printTopList(params, user, ratings):
    Y = params.get('Y')
    movieDict = matrixToCollectionDict(Film)
    user_index = collectionToMatrixDict(User).get(user.id)

    topList = list()
    count = 10
    for item in ratings:
        # item[0] - movie index in matrix
        movie_index = item[0]
        if item[1] < 0 or Y[movie_index, user_index] != 0:
            continue
        movie = movieDict.get(movie_index)
        s = 'Predicting rating %.1f for movie %s (%s)' % (item[1], movie.Title, movie.Year)
        topList.append(s)
        print(s)
        count = count - 1
        if count == 0:
            break
    return topList


def prepareMyPredictions(params, user):
    X = params.get('X')
    Theta = params.get('Theta')
    Ymean = params.get('Ymean')

    p = np.dot(X, Theta.T)

    user_index = collectionToMatrixDict(User).get(user.id)
    my_predictions = p[:, user_index] + Ymean[:, 0]
    return my_predictions


# Based on collection this method transforms entities from db to matrix structure
# This allows us gaps in db data

def collectionToMatrixDict(collection):
    colDict = dict()
    entities = collection.objects.all().order_by('id')
    for row_num, entity in enumerate(entities):
        colDict[entity.id] = row_num
    return colDict


# Based on collection this method reconstruct db entities from matrix structre
# This allows us gaps in db data
def matrixToCollectionDict(collection):
    colDict = dict()
    entities = collection.objects.all().order_by('id')
    for row_num, entity in enumerate(entities):
        colDict[row_num] = entity
    return colDict
