import json
import pickle

import numpy as np
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


def loadRatingsColumns():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    ratings = db.ratings_col
    Y = None
    R = None
    for record in ratings.find():
        cur_Y = pickle.loads(record['Y'])
        Y = addColumn(Y, cur_Y)

        cur_R = pickle.loads(record['R'])
        R = addColumn(R, cur_R)
    return (Y, R)


def addColumn(matrix, newColumn):
    if matrix is not None:
        matrix = np.column_stack((matrix, newColumn))
    else:
        matrix = newColumn
    return matrix
