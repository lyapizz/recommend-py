import json
import urllib.parse
from urllib.request import urlopen

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from pymongo.errors import DuplicateKeyError

from .models import Choice, Question, Film


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
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def importFilms(request):
    fp = open('MoviesIds_all.txt')
    for id in fp:
        try:
            existingFilm = Film.objects.get(imdbID=id)
            print("Film exits in DB", existingFilm.Title)
        except Film.DoesNotExist:
            createNewFilm(id)
    return render(request, template_name='polls/home.html')


def createNewFilm(id):
    urlService = "http://www.omdbapi.com/?"

    params = dict()
    params['i'] = id.strip()
    params['apikey'] = '2f78818b'
    url = urlService + urllib.parse.urlencode(params)

    print('Retreiving url: ', url)

    fp = urllib.request.urlopen(url)

    data = json.load(fp)
    if data['Response'] == "True":

        if int(data['Year']) < 2000:
            print("Film %s is too old for db" % (data["Title"]))
            return

        # insert film to db
        try:
            insertFilm(data)
        except DuplicateKeyError:
            print("Film with title '%s' already exists in db" % (data["Title"]))
    else:
        print("Problem with loading movie:", id)


def insertFilm(data):
    Film.objects.create(Title=data['Title'],
                        Year=data['Year'],
                        Poster=data['Poster'],
                        imdbID=data['imdbID'])
