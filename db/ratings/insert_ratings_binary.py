# todo remove this file after init db
import pickle

import pymongo as pymongo
from bson import Binary
from scipy.io import loadmat

def insert_ratings():
    mat_contents = loadmat('ml/test/resources/ex8_movies.mat')
    (Y, R) = (mat_contents.get("Y"), mat_contents.get("R"))
    insert_matrixes(Y, R)

def insert_matrixes(Y, R):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    ratings = db.ratings

    record = dict()
    record['Y'] = Binary(pickle.dumps(Y, protocol=2))
    record['R'] = Binary(pickle.dumps(R, protocol=2))
    record['name'] = 'default_ratings'
    ratings.insert_one(record)