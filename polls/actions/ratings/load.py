import numpy as np
from django_registration.forms import User

from ..actions import collectionToMatrixDict
from ...models import Film, Ratings


def loadRatings():
    movies = collectionToMatrixDict(Film)
    users = collectionToMatrixDict(User)
    Y = np.zeros((len(movies), len(users)))

    for rating in Ratings.objects.all():
        curMovie = movies.get(rating.film.id)
        curUser = users.get(rating.user.id)
        Y[curMovie, curUser] = rating.score

    R = Y != 0
    return (Y, R)
