
from polls.models import Film


def nextFilm(id):
    film = Film.objects.filter(id__gt=id).filter(Year__lt=2021).order_by('id').first()
    if film is None:
        return -1
    else:
        return film.id


def previousFilm(id):
    film = Film.objects.filter(id__lt=id).filter(Year__lt=2021).order_by('-id').first()
    if film is None:
        return -1
    else:
        return film.id
