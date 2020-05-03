import json
import urllib.parse
from urllib.request import urlopen

from django.conf import settings

from polls.models import Film


def importFilmOMDB(id):
    if Film.objects.filter(imdbID=id).count() > 0:
        print("Film with title '%s' already exists in db" % (id))
        return
    data = getByImdbID(id)
    if data:
        # insert film to db
        obj = Film.objects.create(Year=data['Year'], Poster=data['Poster'], Title=data['Title'],
                                  imdbID=data['imdbID'], imdbUrl='https://www.imdb.com/title/' + data['imdbID'],
                                  Plot=data['Plot'])
        return obj
    else:
        print("Problem with loading movie:", id)


def getByImdbID(id):
    urlService = "http://www.omdbapi.com/?"
    params = dict()
    params['i'] = id.strip()
    params['apikey'] = settings.OMDB_API_KEY
    url = urlService + urllib.parse.urlencode(params)

    print('Retreiving url: ', url)

    fp = urllib.request.urlopen(url)

    data = json.load(fp)
    if data['Response'] == "True":
        return data
    else:
        print("Problem with loading movie:", id)
        return dict()
