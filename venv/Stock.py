from datetime import datetime 
from dateutil.relativedelta import relativedelta
import FinanceDataReader as fdr
class Stock:
    def __init__(self,ticker,name, date):
        self.ticker = ticker
        self.name = name
  
        self.init_date(date)
        self.fdr = fdr.DataReader(str(self.ticker), self.before_1_year)
    def init_date(self, date):
        self.now = date
        before_3_day =  self.now - relativedelta(days=3)
        self.before_1_month = self.now - relativedelta(months=1)
        self.before_3_month = self.now - relativedelta(months=3)
        self.before_6_month = self.now - relativedelta(months=6)
        self.before_1_year = self.now - relativedelta(years=1)
        self.month_1=self.before_1_month.strftime('%Y-%m-%d')
        self.month_3=self.before_3_month.strftime('%Y-%m-%d')
        self.month_6=self.before_6_month.strftime('%Y-%m-%d')
        self.month_12=self.before_1_year.strftime('%Y-%m-%d')
               
    def get_momentum_score(self):
        month_1_df=self.fdr.truncate(after=self.month_1)
        month_3_df=self.fdr.truncate(after=self.month_3)
        month_6_df=self.fdr.truncate(after=self.month_6)
        month_12_df=self.fdr.truncate(before=self.month_12)
 
        today_close = self.get_current_stock_price()
        close_1 =month_1_df.tail(1).iloc[0].Close
        close_3 =month_3_df.tail(1).iloc[0].Close
        close_6 =month_6_df.tail(1).iloc[0].Close
        close_12 =month_12_df.head(1).iloc[0].Close
        
        rate_1= today_close / close_1 -1
        rate_3= today_close / close_3 -1
        rate_6= today_close / close_6 -1
        rate_12= today_close / close_12 -1
        #=(H9*12)+(J9*4)+(M9*2)+(S9*1)
        self.momentum_score = rate_1 * 12 + rate_3 *4 + rate_6 * 2 + rate_12
        return self.momentum_score
    def get_current_stock_price(self):
        return self.fdr.tail(1).iloc[0].Close
    