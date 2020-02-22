import numpy as np
import scipy as scipy

def checkCostFunction(**kwargs):
    lambda_reg = kwargs.get('lambda_reg', 0)
# Create small problem
    X_t = scipy.rand(4, 3)
    Theta_t = scipy.rand(5, 3)
# Zap out most entries
    Y = np.dot(X_t, Theta_t.T)
    Y[scipy.rand(4, 5) > 0.5] = 0

    R = np.zeros(Y.shape)
    R[Y > 0] = 1
