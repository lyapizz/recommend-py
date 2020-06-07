from django.contrib.auth.signals import user_logged_in

from polls.models import Ratings


def save_session_ratings(sender, user, request, **kwargs):
    print("Welcome, " + user.username + ".")
    session_key_copy = request.session.get('key_copy')
    if session_key_copy:
        print("You have some data from session:" + session_key_copy)
        notSavedRatings = Ratings.objects.filter(session=session_key_copy)
        for notSaveRating in notSavedRatings:
            print("film_id=" + str(notSaveRating.film_id) + ",score=" + str(notSaveRating.score))
            Ratings.objects.update_or_create(
                film_id=notSaveRating.film_id,
                user_id=user.id,
                defaults={"score": notSaveRating.score}
            )


user_logged_in.connect(save_session_ratings)
