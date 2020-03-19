import re


def loadMovieList():
    # GETMOVIELIST reads the fixed movie list in movie.txt and returns a
    # cell array of the words
    #   movieList = GETMOVIELIST() reads the fixed movie list in movie.txt
    #   and returns a cell array of the words in movieList.


    ## Read the fixed movieulary list
    fid = open('movie_ids.txt')

    movieList = list()
    for line in fid:
        line = line.strip()
        pieces = re.findall('([0-9]+) (.+)\(([0-9]+)\)', line)

        for movie in pieces:
            filmDict = dict()
            filmDict['Film_ID'] = int(movie[0])
            filmDict['Title'] = movie[1].strip()
            filmDict['Year'] = movie[2]
            movieList.append(filmDict)
    return movieList