from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Film


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
        selected_choice = film.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the film voting form.
        return render(request, 'polls/detail.html', {
            'film': film,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(film.id,)))
