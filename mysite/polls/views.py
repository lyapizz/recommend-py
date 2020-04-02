from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from star_ratings.models import UserRating
from .actions.actions import printTopRecommendations
from .actions.ratings.load import loadRatings
from .ml.train import train
from .models import Film, Rating


def home(request, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, template_name='polls/home.html')


@login_required
def profile(request):
    return render(request, template_name='polls/profile.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_films_list'

    def get_queryset(self):
        """Return the last five films."""
        return Film.objects.order_by('id')[:5]


class DetailView(generic.DetailView):
    model = Film
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Film
    template_name = 'polls/results.html'


def rate(self, instance, score, user=None, ip=None):
    s = score
    s


def vote(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    try:
        user_rating = UserRating.objects.for_instance_by_user(film, user=request.user)
        score = user_rating.score

        existing_rating = Rating.objects.get_or_create(film=film, user=request.user)[0]
        existing_rating.score = score
        existing_rating.save()


    except KeyError:
        # Redisplay the film voting form.
        return render(request, 'polls/detail.html', {
            'film': film,
        })
    else:
        return render(request, 'polls/results.html', {
            'film': film,
            'score': score,
        })


def top(request, **kwargs):
    # this operation should be done in background and updated
    (Y, R) = loadRatings()
    result = train(10, Y=Y, R=R, maxiter=30)
    recommendations = printTopRecommendations(result, request.user)
    return render(request, 'polls/top.html', {
        'recommendations': recommendations
    })
