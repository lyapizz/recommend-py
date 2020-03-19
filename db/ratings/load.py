import time

import numpy as np
import pymongo as pymongo

from db.films.load_films import loadFilmsMap


def loadRatings():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    ratings = db.ratings
    Y = None
    movieList = loadFilmsMap()

    for record in ratings.find():
        cur_Y_dict = record['Y']
        cur_Y = restoreNulls(cur_Y_dict, len(movieList))
        Y = addColumn(Y, cur_Y)

    R = Y != 0
    return (Y, R)

def restoreNulls(cur_Y_dict, num_movies):
    #  Initialize my ratings
    cur_Y = np.zeros(num_movies, dtype=np.uint8)
    # Check the file movie_idx.txt for id of each movie in our dataset
    # For example, Toy Story (1995) has ID 1, so to rate it "4", you can set
    for k,v in cur_Y_dict.items():
        cur_Y[int(k)] = v
    return cur_Y

def addColumn(matrix, newColumn):
    if matrix is not None:
        matrix = np.column_stack((matrix, newColumn))
    else:
        matrix = newColumn
    return matrix
