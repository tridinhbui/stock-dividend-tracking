import pandas as pd
import numpy as np
import datetime as dt# Xử lý ngày tháng
# import investpy 
from vnstock import *

print(ticker_overview('TCB'))
print(price_board('TCB,SSI,VND'))
df =  stock_historical_data(symbol='GMD', 
                            start_date="2021-01-01", 
                            end_date='2022-02-25'))
print(df.head())
# start = "01/01/2015"
# end  = dt.datetime.now().strftime("%d/%m/%Y")
# company = "CTG"
# CTG = investpy.get_stock_recent_data(stock= company, country= 'vietnam')              
# CTG.head()

# ACB = investpy.get_stock_historical_data(stock= "ACB", country= 'vietnam', from_date = start, to_date = end)
                                        
# ACB.drop("Currency", axis = 1, inplace = True)
# ACB.head()