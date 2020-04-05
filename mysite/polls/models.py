from django.db import models
from django_registration.forms import User

from star_ratings.models import AbstractBaseRating, RatingManager


class MyRatingManager(RatingManager):
    def rate(self, instance, score, user=None, ip=None):
        if isinstance(instance, self.model):
            raise TypeError("Rating manager 'rate' expects model to be rated, not Rating model.")

        existing_rating = Rating.objects.get_or_create(film=instance, user=user)[0]
        existing_rating.score = score
        existing_rating.save()
        return existing_rating

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


class MyRating(AbstractBaseRating):
    average = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)

    objects = MyRatingManager()


# two ratings are too much
class Rating(models.Model):
    score = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, default=1)
    objects = models.Manager

    def to_dict(self):
        return {
            'score': self.score,
            'user': self.user.id,
            'film': self.film.id,
        }

# class GlobalRatings(models.Model):
#     film = models.ForeignKey(Film, on_delete=models.CASCADE)
#     source = models.CharField(max_length=200)
#     value = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.film.__str__() + self.source + self.value
