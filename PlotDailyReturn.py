import matplotlib.pyplot as plt
from LoadReturn import LoadReturnData

class PlotPriceData:
    
    def PlotDailyPrice():
        print('PlotDailyReturn')
        ret = LoadReturnData.loadDailyReturn()
        
        ret_index = ret.set_index('date')
        table = ret_index.pivot(columns ='ticker')        
        
        table.coulmns = [col[1] for col in table.columns]  
        
        plt.figure (figsize =(14,7))
        for prc in table.columns.values:
            plt.plot(table.index, table[prc], lw=3, alpha=0.8, label=prc)
        plt.legend(loc='upper left', fontsize =12)
        plt.ylabel ('Price')        
   
    PlotDailyPrice()