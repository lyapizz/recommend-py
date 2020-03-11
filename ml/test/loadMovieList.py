import re

from db.objects.film import Film


def loadMovieList():
    # GETMOVIELIST reads the fixed movie list in movie.txt and returns a
    # cell array of the words
    #   movieList = GETMOVIELIST() reads the fixed movie list in movie.txt
    #   and returns a cell array of the words in movieList.


    ## Read the fixed movieulary list
    fid = open('movie_ids.txt')

    movieList = dict()
    for line in fid:
        line = line.strip()
        pieces = re.findall('([0-9]+) (.+)', line)
        for movie in pieces:
            movieList[int(movie[0])] = movie[1]
    return movieList

def loadMovieListObj():
    # GETMOVIELIST reads the fixed movie list in movie.txt and returns a
    # cell array of the words
    #   movieList = GETMOVIELIST() reads the fixed movie list in movie.txt
    #   and returns a cell array of the words in movieList.


    ## Read the fixed movieulary list
    fid = open('movie_ids.txt')

    movieList = dict()
    for line in fid:
        line = line.strip()
        pieces = re.findall('([0-9]+) (.+)\(([0-9]+)\)', line)

        for movie in pieces:
            film = Film(int(movie[0]), movie[1].strip(), int(movie[2]))
            movieList[film.film_ID] = film
    return movieList

