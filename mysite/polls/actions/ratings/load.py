import numpy as np
from django_registration.forms import User

from ...models import Film, Rating


def loadRatings():
    movies = Film.objects.all()
    users = User.objects.all()
    Y = np.zeros((movies.count(), users.count()))

    for rating in Rating.objects.all():
        curMovie = rating.film.id
        curUser = rating.user.id
        Y[curMovie - 1, curUser - 1] = rating.score

    R = Y != 0
    return (Y, R)
