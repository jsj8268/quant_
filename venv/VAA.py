from Stock import Stock
import FinanceDataReader as fdr
import pandas as pd
from datetime import datetime 
import pprint as pp
class VAA:
    ATTCK = 1
    DEFECCE = -1
    MIDDLE = 0
   
    def __init__(self) :
        self.stocks = {}
     
    def add_stock(self , ticker , name , date):
        stock = Stock(ticker , name , date)
        self.stocks[ticker] = stock
        
    def get_today_stock(self ):
        attack =self.df.iloc[0:4]
        attack['momntum_score'] < 0
       
        min = attack.loc[attack['momntum_score'] < 0]
        index = 0
        if len(min)==0:
           #return attack['momntum_score'].max()
           index = attack['momntum_score'].idxmax()
           return  attack.loc[index]
        else: 
            defence = self.df.iloc[4:7]
            #return defence['momntum_score'].max()
            index=  defence['momntum_score'].idxmax()
            return  defence.loc[index]
            
    def make_data_frame(self):
        column_names = ['ticker','momntum_score','price','name'] 
        data = []       
        record = []
        for k , v in self.stocks.items():
            record = []
            score = v.get_momentum_score()
            price = v.get_current_stock_price()
            record.append(k)   
            record.append(score)
            record.append(price)
            record.append(v.name)
            data.append(record)
      
        self.df = pd.DataFrame(data,columns=column_names)
        pp.pprint(self.df)

        
stocks = {143850:'KODEX 미국 S&P500선물(H)',251350:'KODEX 선진국MSCI World',195980:'ARIRANG 신흥국MSCI(합성h)',273130:'종합채권',332620:'ARIRANG 미국장기우량회사채',305080:'TIGER 미국채 10년 선물',329750:'TIGER 미국달러단기채권엑티브'}
vaa = VAA()
stocks[143850]
for k ,v in stocks.items():
    now = datetime.now()
    vaa.add_stock(k,v,now)

vaa.make_data_frame()
pp.pprint(vaa.get_today_stock())