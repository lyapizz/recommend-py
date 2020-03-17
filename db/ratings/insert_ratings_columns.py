# todo remove this file after init db
import pickle

import pymongo as pymongo
from bson import Binary
from scipy.io import loadmat

from db.users.actions import get_user_by_name


def insert_ratings_from_file():
    mat_contents = loadmat('ml/test/resources/ex8_movies.mat')
    (Y, R) = (mat_contents.get("Y"), mat_contents.get("R"))
    insert_matrixes(Y, R)

def insert_matrixes(Y, R):

    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    ratings = db.ratings_col

    num_users = Y.shape[1]
    for user_id in range(num_users):
        insert_ratings_to_DB(R[:, user_id], Y[:, user_id], ratings, user_id)

def insert_ratings(ratings, user_name):
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    table = db.ratings_col

    user = get_user_by_name(user_name)
    Ycol = ratings
    Rcol = ratings != 0
    insert_ratings_to_DB(Rcol, Ycol, table, user["user_ID"])


def insert_ratings_to_DB(Rcol, Ycol, table, user_id):
    record = dict()
    record['Y'] = Binary(pickle.dumps(Ycol, protocol=2))
    record['R'] = Binary(pickle.dumps(Rcol, protocol=2))
    record['user_id'] = user_id
    table.insert_one(record)


#insert_ratings_from_file()