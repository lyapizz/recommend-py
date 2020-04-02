import json

from frontend.mysite.polls.db.ratings.insert import insert_ratings
from frontend.mysite.polls.db.users.actions import get_user_by_name

name = input("Enter your name: ")
# name = 'lyapizz'

user = get_user_by_name(name)

if (user is None):
    print("Oh, new user! Welcome, %s" % name)
    ## ============== Part 6: Entering ratings for a new user ===============
    fp = open('my_ratings.json')
    my_ratings = json.load(fp)

    # insert user to db
    # insert_user(name)
    # insert his ratings to db
    insert_ratings(my_ratings, name)
else:
    print("Welcome back, %s" % name)
#
# ================== Part 7: Learning Movie Ratings ====================
#  Now, you will train the collaborative filtering model on a movie rating 
#  dataset of 1682 movies and 943 users
#
fp = open('my_ratings_sample.json')
my_ratings = json.load(fp)
insert_ratings(my_ratings, name)

# result = train(10, maxiter=30)
# result = train(10, my_ratings=my_ratings, maxiter=30)

## ================== Part 8: Recommendation for you ====================
#  After training the model, you can now make recommendations by computing
#  the predictions matrix.
#

# printTopRecommendations(result, name)

#print('Cost function:', result.get('J'))
print('Success!')
