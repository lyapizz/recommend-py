from numpy import mean, zeros


def normalizeRatings(Y, R):
    # NORMALIZERATINGS Preprocess data by subtracting mean rating for every
    # movie (every row)
    #   [Ynorm, Ymean] = NORMALIZERATINGS(Y, R) normalized Y so that each movie
    #   has a rating of 0 on average, and returns the mean rating in Ymean.
    #

    # m films, n - users
    (m, n) = Y.shape
    Ymean = zeros((m, 1))
    Ynorm = zeros(Y.shape)
    for i in range(m):
        idx = R[i, :] == 1
        if Y[i, idx].size:
            Ymean[i] = mean(Y[i, idx])
            Ynorm[i, idx] = Y[i, idx] - Ymean[i]
    return (Ynorm, Ymean)