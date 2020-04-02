import pymongo as pymongo


def get_table():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.recommend_local
    return db.auth_user


# def insert_default_users():
#   users = get_table()
#   num_users = 943
#
#   for i in range(0, num_users):
#     user = User(users.count_documents({}), 'user_' + str(i))
#     users.insert_one(user.__dict__)
#
# def insert_user(name):
#   users = get_table()
#   user = User(users.count_documents({}), name)
#   get_table().insert_one(user.__dict__)

def get_user_by_name(name):
    users = get_table()
    for user in users.find({"username": name}):
        return user
