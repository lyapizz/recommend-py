Don't know which film to watch tonight? Use recommend-py to know it.

**HowTO:**

1) Download the source code,
2) Modify sample file: `my_ratings.json` with your film ratings:
  a) Set number for 1 to 5 to a film according to list of films in `movie_ids.txt`.
  For example, Toy Story (1995) has ID 0, so to rate it "4", you can add row "0": 4 in `my_ratings.json`.
3) More rating, more precise result.

As output you will get top 10 recommendations based on your ratings using collaborative filtering algorithm.

**What's next:**
- DB to store users and films. Currently I consider mongoDB for it
- User Interface for voting for a film
- New modern films, currently all films in db are below 2000 year.
