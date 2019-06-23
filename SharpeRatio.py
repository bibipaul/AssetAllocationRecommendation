import numpy as np
from StandardDeviation import StandardDeviation

class SharpeRatio:    

    def DeriveSharpeRatio(num_portfolios, mean_returns,
                          cov_matrix, risk_free_rate):
        results = np.zeros((3,num_portfolios))
        weights_record = []
        for i in range(num_portfolios):
            weights = np.random.random(4)
            weights /=np.sum(weights)
            weights_record.append(weights)
            portfoli_std_dev, portfolio_return = StandardDeviation.CalcStandardDeviation(weights, mean_returns, cov_matrix)
            results[0,i] = portfoli_std_dev
            results[1,i] = portfolio_return
            results[2,i] = (portfolio_return - risk_free_rate)/portfoli_std_dev
           
            return  results, weights_record