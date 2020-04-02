from django.db import models
from django_registration.forms import User

from star_ratings.models import AbstractBaseRating


class MyRating(AbstractBaseRating):
    average = models.PositiveIntegerField(default=0)

class Film(models.Model):
    Title = models.CharField(max_length=200)
    Year = models.CharField(max_length=200, default="0")
    # rated = models.CharField(max_length=200)
    # released = models.DateTimeField
    # runtime = models.CharField(max_length=200)
    # genre = models.CharField(max_length=200)
    # director = models.CharField(max_length=200)
    # writer = models.CharField(max_length=200)
    # actors = models.CharField(max_length=200)
    # plot = models.CharField(max_length=200)
    # language = models.CharField(max_length=200)
    # country = models.CharField(max_length=200)
    # awards = models.CharField(max_length=200)
    Poster = models.CharField(max_length=1000)
    # metascore = models.CharField(max_length=200)
    # imdbRating = models.CharField(max_length=200)
    # imdbVotes = models.CharField(max_length=200)
    imdbID = models.CharField(max_length=200, default="")

    # type = models.CharField(max_length=200)
    # DVD = models.DateTimeField
    # boxOffice = models.CharField(max_length=200)
    # production = models.CharField(max_length=200)
    # website = models.CharField(max_length=200)

    objects = models.Manager

    def __str__(self):
        return self.Title


class Rating(models.Model):
    score = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    objects = models.Manager

# class GlobalRatings(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE)
#     source = models.CharField(max_length=200)
#     value = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.film.__str__() + self.source + self.value
