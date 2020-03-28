from django.db import models

from star_ratings.models import AbstractBaseRating
from django.db import models

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

    def __str__(self):
        return self.Title


class Choice(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# class GlobalRatings(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE)
#     source = models.CharField(max_length=200)
#     value = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.film.__str__() + self.source + self.value
