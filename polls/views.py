from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .actions.actions import printTopRecommendations
from .actions.ratings.load import loadRatings
from .ml.train import train
from .models import Film
from .utils import nextFilm, previousFilm


def home(request, **kwargs):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return render(request, template_name='polls/home.html')


@login_required
def profile(request):
    return render(request, template_name='polls/profile.html')


def contact(request):
    return render(request, template_name='polls/contact.html')


def about(request):
    return render(request, template_name='polls/about.html')


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_films_list'

    def get_queryset(self):
        return Film.objects.filter(Year__lt=2021).order_by('id')


@login_required
def detail(request, **kwargs):
    id = kwargs['id']
    action = kwargs.get('action')
    if action is None:
        film = Film.objects.get(id=id)
        return render(request, 'polls/detail.html',
                      {'film': film, 'prevFilm': previousFilm(id), 'nextFilm': nextFilm(id)})
    filmToMove = None
    if action == 'next':
        filmToMove = nextFilm(id)
    elif action == 'previous':
        filmToMove = previousFilm(id)

    pk = id
    if filmToMove is not None:
        pk = filmToMove.id
    return HttpResponseRedirect(reverse('polls:detail', args={pk}))


@login_required
def top(request, **kwargs):
    # this operation should be done in background and updated
    (Y, R) = loadRatings()
    result = train(Y, R)
    recommendations = printTopRecommendations(result, request.user)
    return render(request, 'polls/top.html', {
        'recommendations': recommendations
    })
