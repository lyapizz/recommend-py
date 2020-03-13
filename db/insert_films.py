# Connect to MongoDB instance running on cloud
import json
import pymongo as pymongo
from ml.test.loadMovieList import loadMovieList

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.recommend_local
films = db.films

moviesFromFile = loadMovieList()
for v in moviesFromFile.values():
  films.insert_one(v.__dict__)