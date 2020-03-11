# Connect to MongoDB instance running on cloud
import json
import pymongo as pymongo
from ml.test.loadMovieList import loadMovieListObj

client = pymongo.MongoClient("mongodb+srv://lyapizz:1c2d3e4f5g6a7h@cluster-films-9ngvc.mongodb.net/test?retryWrites=true&w=majority")
db = client.recommend
films = db.films

moviesFromFile = loadMovieListObj()

filmDocumentTemplate = {
  "film_ID": 0,
  "title": "Toy Story",
  "year": 1995
}

for v in moviesFromFile.values():
  films.insert_one(v.__dict__)


