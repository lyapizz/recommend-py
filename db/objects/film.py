import json


class Film:
    film_ID = -1
    title = ""
    year = 0

    def __init__(self, film_ID, title, year):
        self.film_ID = film_ID
        self.title = title
        self.year = year

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)