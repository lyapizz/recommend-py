# todo remove this file after init db

import pymongo as pymongo

from db.objects.user import User

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client.recommend_local
users = db.users

num_users = 943

for i in range(1, num_users+1):
  user = User(i, 'user_'+str(i))
  users.insert_one(user.__dict__)