import pickle

import pymongo as pymongo
from bson import Binary
from scipy.io import loadmat

from db.users.actions import get_user_by_name

def getCollection():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    return db.ratings

def insert_ratings_from_file():
    mat_contents = loadmat('ml/test/resources/ex8_movies.mat')
    insert_matrixes(mat_contents.get("Y"))


def convertToDict(lst):
    result = dict()
    for i in range(len(lst)):
        if lst[i] != 0:
            result[str(i)] = lst[i]
    return result


def insert_matrixes(Y):
    ratings = getCollection()
    num_users = Y.shape[1]
    for user_id in range(num_users):
        Ydict = convertToDict(Y[:, user_id].tolist())
        insert_ratings_to_DB(Ydict, ratings, user_id)

def insert_ratings(ratings, user_name):
    table = getCollection()
    user = get_user_by_name(user_name)
    insert_ratings_to_DB(ratings, table, user["user_ID"])


def insert_ratings_to_DB(Ycol, table, user_id):
    record = dict()
    record['Y'] = Ycol
    record['user_ID'] = user_id
    table.insert_one(record)
