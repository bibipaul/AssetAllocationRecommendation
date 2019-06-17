import quandl
import pandas as pd
import os

class LoadReturnData:
    def ImportDailyReturn():
        quandl.ApiConfig.api_key='Paste Your quandl Key'
        stocks =['AAPL','AMZN','GOOGL','FB']
        data =quandl.get_table('WIKI/PRICES', ticker=stocks, qopts={'columns': ['date', 'ticker', 'adj_close']}
                      , date ={'gte': '2018-1-1', 'lte': '2018-12-31'}, paginate=True)
        data.to_csv(r'$your path\DailyReturn.xls')
            
    def loadDailyReturn():
        csv_path =os.path.join("$your path","DailyReturn.xls")
        df = pd.read_csv(csv_path)        
        return df
        
#    ImportDailyReturn()
#    data=loadDailyReturn()
#    data.info()
                
    
