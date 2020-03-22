import json

from activities.actions import printTopRecommendations
from db.ratings.insert import insert_ratings
from db.users.actions import get_user_by_name
from ml.train import train

name = input("Enter your name: ")
# name = 'lyapizz'

user = get_user_by_name(name)

if (user is None):
    print("Oh, new user! Welcome, %s" % name)
    ## ============== Part 6: Entering ratings for a new user ===============
    fp = open('my_ratings.json')
    my_ratings = json.load(fp)

    # insert user to db
    insert_user(name)
    # insert his ratings to db
    insert_ratings(my_ratings, name)
else:
    print("Welcome back, %s" % name)
#
# ================== Part 7: Learning Movie Ratings ====================
#  Now, you will train the collaborative filtering model on a movie rating 
#  dataset of 1682 movies and 943 users
#

result = train(10, maxiter=30)
# result = train(10, my_ratings=my_ratings, maxiter=30)

## ================== Part 8: Recommendation for you ====================
#  After training the model, you can now make recommendations by computing
#  the predictions matrix.
#

printTopRecommendations(result, name)

print('Cost function:', result.get('J'))
print('Success!')
