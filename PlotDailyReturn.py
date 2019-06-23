import matplotlib.pyplot as plt
from ReturnDataSet import ReturnDataSet

class PlotPriceData:
    
    def PlotDailyPrice():
        print('PlotDailyReturn')
        table =ReturnDataSet.DeriveReturnDataSet() 
        
        plt.figure (figsize =(14,7))
        for prc in table.columns.values:
            plt.plot(table.index, table[prc], lw=3, alpha=0.8, label=prc)
        plt.legend(loc='upper left', fontsize =12)
        plt.ylabel ('Price')        
   
    PlotDailyPrice()