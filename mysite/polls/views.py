from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .actions.actions import printTopRecommendations
from .actions.ratings.load import loadRatings
from .ml.train import train
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

def top(request, **kwargs):
    # this operation should be done in background and updated
    (Y, R) = loadRatings()
    result = train(10, Y=Y, R=R, maxiter=30)
    recommendations = printTopRecommendations(result, request.user)
    return render(request, 'polls/top.html', {
        'recommendations': recommendations
    })
