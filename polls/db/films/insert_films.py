import pymongo as pymongo

from ...ml.test.loadMovieList import loadMovieList


def getCollection():
  client = pymongo.MongoClient("mongodb://localhost:27017")
  db = client.recommend_local
  return db.films

def insertDefaultFilms():
  films = getCollection()

  moviesFromFile = loadMovieList()
  for filmDict in moviesFromFile:
    films.insert_one(filmDict)

def insertFilm(data):
  films = getCollection()
  data['Film_ID'] = films.count_documents({})
  films.insert_one(data)