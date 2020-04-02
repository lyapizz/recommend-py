from ...models import Film


def loadFilmsMap():
    filmsDict = dict()
    for film in Film.objects.all():
        filmsDict[film.id] = film

    return filmsDict
