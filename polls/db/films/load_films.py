import pymongo as pymongo


def loadFilmsMap():
    client = pymongo.MongoClient("mongodb://localhost:27018")
    db = client.recommend_local
    films = db.films

    filmsDict = dict()
    for film_data in films.find():
        filmsDict[film_data["Film_ID"]] = film_data

    return filmsDict
