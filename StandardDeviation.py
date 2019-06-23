import numpy as np

class StandardDeviation:
    
    def CalcStandardDeviation(weights, mean_returns, cov_matrix):
        returns = np.sum(mean_returns * weights) * 252
        std = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights))) * np.sqrt(252)
        
        return std, returns
        