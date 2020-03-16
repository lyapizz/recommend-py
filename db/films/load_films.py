import json
import pymongo as pymongo
from bson import json_util
from bson.json_util import dumps

from db.objects.film import Film

def loadFilmsMap():
  client = pymongo.MongoClient("mongodb://localhost:27017")
  db = client.recommend_local
  films = db.films

  filmsDict = dict()
  for film_data in films.find():
    #from dict to str
    film_str = dumps(film_data)
    #from str to json
    #todo think about creating object from dict
    film = Film(**json.loads(film_str, object_hook=json_util.object_hook))
    filmsDict[film.film_ID] = film

  return filmsDict