import json


class Film:
    film_ID = -1
    title = ""
    year = 0

    def __init__(self, film_ID, title, year, _id=None):
        self.film_ID = film_ID
        self.title = title
        self.year = year