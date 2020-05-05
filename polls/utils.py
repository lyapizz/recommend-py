
from polls.models import Film


def nextFilm(id):
    return Film.objects.filter(id__gt=id).filter(Year__lt=2021).order_by('id').first()

def previousFilm(id):
    return Film.objects.filter(id__lt=id).filter(Year__lt=2021).order_by('-id').first()
