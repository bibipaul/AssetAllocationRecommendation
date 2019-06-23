import numpy as np
import pandas as pd
from ReturnDataSet import ReturnDataSet
from SharpeRatio import SharpeRatio

class AssetAllocation:
    
    def PortfolioRecommendation():
        
        table = ReturnDataSet.DeriveReturnDataSet()           
        returns_data = table.pct_change()
        mean_returns = returns_data.mean()
        cov_matrix = returns_data.cov()    
        num_portfolios = 25000
        risk_free_rate = 0.0178
        
        results, weights = SharpeRatio.DeriveSharpeRatio(num_portfolios,mean_returns,
                                      cov_matrix,risk_free_rate)
        
        max_sharpe_idx = np.argmax(results[2])
#        sdp, rp = results[0,max_sharpe_idx], results[1,max_sharpe_idx]
        max_sharpe_allocation = pd.DataFrame(weights[max_sharpe_idx],index=table.columns,columns=['allocation'])
        max_sharpe_allocation.allocation = [round(i*100,2)for i in max_sharpe_allocation.allocation]
        max_sharpe_allocation = max_sharpe_allocation.T
        
#        min_vol_idx = np.argmin(results[0])
#        sdp_min, rp_min = results[0,min_vol_idx], results[1,min_vol_idx]
#        min_vol_allocation = pd.DataFrame(weights[min_vol_idx],index=table.columns,columns=['allocation'])
#        min_vol_allocation.allocation = [round(i*100,2)for i in min_vol_allocation.allocation]
#        min_vol_allocation = min_vol_allocation.T
        
        print ("-"*80)
        print ("Maximum Sharpe Ratio Portfolio Allocation\n")
#        print ("Annualised Return:", round(rp,2))
#        print ("Annualised Volatility:", round(sdp,2))
        print ("\n")
        print (max_sharpe_allocation)
        print ("-"*80)
#        print ("Minimum Volatility Portfolio Allocation\n")
#        print ("Annualised Return:", round(rp_min,2))
#        print ("Annualised Volatility:", round(sdp_min,2))
#        print ("\n")
#        print (min_vol_allocation)
               
    PortfolioRecommendation()
    