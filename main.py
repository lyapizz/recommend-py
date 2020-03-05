from activities.actions import addNewRecommendations, printTopRecommendations
from ml.train import train

## ============== Part 6: Entering ratings for a new user ===============
my_ratings = addNewRecommendations()
#
# ================== Part 7: Learning Movie Ratings ====================
#  Now, you will train the collaborative filtering model on a movie rating 
#  dataset of 1682 movies and 943 users
#
result = train(10, my_ratings=my_ratings, maxiter=10)

## ================== Part 8: Recommendation for you ====================
#  After training the model, you can now make recommendations by computing
#  the predictions matrix.
#
printTopRecommendations(result)

print('Cost function:', result.get('J'))
print('Success!')
