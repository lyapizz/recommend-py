from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from star_ratings.models import UserRating
from .models import Film


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


def vote(request, film_id):
    film = get_object_or_404(Film, pk=film_id)
    try:
        user_rating = UserRating.objects.for_instance_by_user(film, user=request.user)
        score = user_rating.score
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
    return render(request, 'polls/top.html')
