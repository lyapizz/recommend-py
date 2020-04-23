import json
import os
import sys
import urllib.parse
from urllib.request import urlopen

from django.db.transaction import non_atomic_requests

from polls.models import Film


@non_atomic_requests
def importFilmOMDB(id):
    if Film.objects.filter(imdbID=id).count() > 0:
        print("Film with title '%s' already exists in db" % (id))
        return
    urlService = "http://www.omdbapi.com/?"
    params = dict()
    params['i'] = id.strip()
    params['apikey'] = os.environ.get('OMDB_API_KEY')
    url = urlService + urllib.parse.urlencode(params)

    print('Retreiving url: ', url)

    fp = urllib.request.urlopen(url)

    data = json.load(fp)
    if data['Response'] == "True":
        # insert film to db
        for count in range(183):  # remove it after sync up autogen id
            try:
                obj = Film.objects.create(Year=data['Year'], Poster=data['Poster'], Title=data['Title'],
                                          imdbID=data['imdbID'])
                return obj
            except:
                print("try with count = %s ,exception= %s " % (count, sys.exc_info()[0]))
    else:
        print("Problem with loading movie:", id)
