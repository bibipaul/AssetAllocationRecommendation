from LoadReturn import LoadReturnData

class ReturnDataSet:
    
    def DeriveReturnDataSet():
        ret = LoadReturnData.loadDailyReturn()
        
        ret_index = ret.set_index('date')
        table = ret_index.pivot(columns ='ticker')        
        
        table.coulmns = [col[1] for col in table.columns]  
        return table
    
        
        