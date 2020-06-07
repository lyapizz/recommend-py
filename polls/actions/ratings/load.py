import numpy as np
from django_registration.forms import User

from ..actions import collectionToMatrixDict, getSessions
from ...models import Film, Ratings


def loadRatings():
    movies = collectionToMatrixDict(Film)
    users = collectionToMatrixDict(User)
    sessions = getSessions(len(users))

    Y = np.zeros((len(movies), len(users) + len(sessions)), dtype=int)

    for rating in Ratings.objects.all():
        curMovie = movies.get(rating.film_id)
        if rating.user_id:
            curUser = users.get(rating.user_id)
        else:
            curUser = sessions.get(rating.session)
        Y[curMovie, curUser] = rating.score

    R = Y != 0
    return (Y, R)
