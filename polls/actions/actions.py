import numpy as np
from django_registration.forms import User

# This method return top recommendations for exact user
# using already trained model
from ..models import Film, Ratings


def printTopRecommendations(params, request):
    print('\nTop recommendations for %s :\n' % request.user.username)

    my_predictions = prepareMyPredictions(params, request)
    ratings = sorted(enumerate(my_predictions), key=lambda x: x[1], reverse=True)

    return printTopList(params.get('Y'), request, ratings)


def printTopList(Y, request, ratings):
    movieDict = matrixToCollectionDict(Film)
    user_index = getUserIndex(request)

    topList = list()
    count = 10
    for item in ratings:
        # item[0] - movie index in matrix
        movie_index = item[0]
        if item[1] < 0 or Y[movie_index, user_index] != 0:
            continue
        movie = movieDict.get(movie_index)
        s = 'Predicting rating %.1f for movie %s (%s)' % (item[1], movie.Title, movie.Year)  # only for debug
        topList.append((item[1], movie))
        print(s)
        count = count - 1
        if count == 0:
            break
    return topList


def prepareMyPredictions(params, request):
    X = params.get('X')
    Theta = params.get('Theta')
    Ymean = params.get('Ymean')

    p = np.dot(X, Theta.T)

    user_index = getUserIndex(request)
    my_predictions = p[:, user_index] + Ymean[:, 0]
    return my_predictions


def getUserIndex(request):
    usedDict = collectionToMatrixDict(User)
    if request.user.id:
        user_index = usedDict.get(request.user.id)
    else:
        user_index = getSessions(len(usedDict)).get(request.session.session_key)
    return user_index


# Based on collection this method transforms entities from db to matrix structure
# This allows us gaps in db data

def collectionToMatrixDict(collection):
    colDict = dict()
    entities = collection.objects.all().order_by('id')
    for row_num, entity in enumerate(entities):
        colDict[entity.id] = row_num
    return colDict


# session_key -> matrix structure id
def getSessions(auth_users_len):
    sessions = dict()
    entities = Ratings.objects.exclude(session__isnull=True).values('session').order_by('session').distinct()
    for entity in entities:
        sessions[entity['session']] = auth_users_len + len(sessions)
    return sessions


# Based on collection this method reconstruct db entities from matrix structre
# This allows us gaps in db data
def matrixToCollectionDict(collection):
    colDict = dict()
    entities = collection.objects.all().order_by('id')
    for row_num, entity in enumerate(entities):
        colDict[row_num] = entity
    return colDict
