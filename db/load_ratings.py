import json
import pickle

import pymongo as pymongo
from bson import json_util
from bson.json_util import dumps

from db.objects.film import Film

def loadRatingsBinary():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    ratings = db.ratings

    for record in ratings.find({"name": "default_ratings"}):
      Y = pickle.loads(record['Y'])
      R = pickle.loads(record['R'])
      return (Y, R)