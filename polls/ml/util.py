import numpy as np
def filterFilmsWithoutReview(Y, R, minimumReviewsCount):
    R[np.sum(R, axis=1) < minimumReviewsCount] = 0
    return R