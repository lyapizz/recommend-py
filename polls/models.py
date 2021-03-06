from django.contrib.contenttypes.models import ContentType
from django.db import models
from django_registration.forms import User

from star_ratings import app_settings
from star_ratings.models import AbstractBaseRating, RatingManager


class MyRatingManager(RatingManager):

    def rate(self, instance, score, user=None, ip=None):
        existing_rating = Ratings.objects.get_or_create(film=instance, user=user)[0]
        if existing_rating.score == score:
            existing_rating.score = 0
        else:
            existing_rating.score = score
        existing_rating.save()
        return existing_rating



class Film(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=200, default="0")
    # rated = models.CharField(max_length=200)
    # released = models.DateTimeField
    # runtime = models.CharField(max_length=200)
    genre = models.CharField(max_length=200, null=True)
    # director = models.CharField(max_length=200)
    # writer = models.CharField(max_length=200)
    # actors = models.CharField(max_length=200)
    Plot = models.CharField(max_length=1000, null=False)
    # language = models.CharField(max_length=200)
    # country = models.CharField(max_length=200)
    # awards = models.CharField(max_length=200)
    Poster = models.CharField(max_length=1000)
    # metascore = models.CharField(max_length=200)
    # imdbRating = models.CharField(max_length=200)
    # imdbVotes = models.CharField(max_length=200)
    imdbID = models.CharField(max_length=200, default="", null=False)
    imdbUrl = models.CharField(max_length=1000, null=False,
                               verbose_name="IMDB url")  # my custom field to add film by imdbUrl

    # type = models.CharField(max_length=200)
    # DVD = models.DateTimeField
    # boxOffice = models.CharField(max_length=200)
    # production = models.CharField(max_length=200)
    # website = models.CharField(max_length=200)

    objects = models.Manager

    def next(self):
        film = Film.objects.filter(id__gt=self.id).filter(Year__lt=2021).order_by('id').first()
        if film is None:
            return -1
        else:
            return film.id

    def previous(self):
        film = Film.objects.filter(id__lt=self.id).filter(Year__lt=2021).order_by('-id').first()
        if film is None:
            return -1
        else:
            return film.id

    def __str__(self):
        return self.Title


class MyRating(AbstractBaseRating):
    # override to avoid decimal exception in mongo
    average = models.PositiveIntegerField(default=0)
    count = models.PositiveIntegerField(default=1)

    objects = MyRatingManager()


class Ratings(models.Model):
    score = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings', null=True, blank=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1, related_name='ratings')
    session = models.CharField(max_length=1000, null=True)

    objects = models.Manager

    def percentage(self):
        return (self.score / app_settings.STAR_RATINGS_RANGE) * 100

    def to_dict(self):
        return {
            'percentage': self.percentage(),
            'user_rating': self.score
        }