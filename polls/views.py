import json
import time

from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import generic, View

from star_ratings import get_star_ratings_rating_model, app_settings
from star_ratings.compat import is_authenticated
from star_ratings.forms import CreateUserRatingForm
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


class Rate(View):
    model = get_star_ratings_rating_model()

    def get_object(self):
        """
        Returns the model instance we're rating from the URL params.
        """
        content_type = ContentType.objects.get_for_id(self.kwargs.get('content_type_id'))
        return content_type.get_object_for_this_type(pk=self.kwargs.get('object_id'))

    def post(self, request, *args, **kwargs):
        def _post(request, *args, **kwargs):
            startTime = time.time()
            data = request.POST or json.loads(request.body.decode())

            return_url = data.pop('next', '/')
            if 'HTTP_X_REAL_IP' in self.request.META:
                data['ip'] = self.request.META['HTTP_X_REAL_IP']
            else:
                data['ip'] = self.request.META['REMOTE_ADDR']

            data['user'] = is_authenticated(request.user) and request.user.pk or None

            res_status = 200

            try:
                form = CreateUserRatingForm(data=data, obj=self.get_object())
                if form.is_valid():
                    rating = form.save()
                    result = rating.to_dict()
                    result['user_rating'] = int(form.cleaned_data['score'])
                else:
                    result = {'errors': form.errors}
                    res_status = 400
            except ValidationError as err:
                result = {'errors': err.message}
                res_status = 400

            if request.is_ajax():
                response = JsonResponse(data=result, status=res_status)
                print("--- %s seconds for full rate.view ---" % (time.time() - startTime))

                return response
            else:
                return HttpResponseRedirect(return_url)

        if not app_settings.STAR_RATINGS_ANONYMOUS:
            return login_required(_post)(request, *args, **kwargs)

        return _post(request, *args, **kwargs)
