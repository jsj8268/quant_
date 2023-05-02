import FinanceDataReader as fdr
from datetime import datetime 
from dateutil.relativedelta import relativedelta



       
stocks = {143850:'KODEX 미국 S&P500선물(H)',251350:'KODEX 선진국MSCI World',195980:'ARIRANG 신흥국MSCI(합성h)',273130:'종합채권',332620:'ARIRANG 미국장기우량회사채',305080:'TIGER 미국채 10년 선물',329750:'TIGER 미국달러단기채권엑티브'}
#stocks = {'SPY':'KODEX 미국 S&P500선물(H)',"EFA":'KODEX 선진국MSCI World','EEM':'ARIRANG 신흥국MSCI(합성h)','AGG':'종합채권','LQD':'ARIRANG 미국장기우량회사채','IEF':'TIGER 미국채 10년 선물','SHY':'TIGER 미국달러단기채권엑티브'}
now = datetime.now()
before_3_day =  now - relativedelta(days=3)
before_1_month = now - relativedelta(months=1)
before_3_month = now - relativedelta(months=3)
before_6_month = now - relativedelta(months=6)
before_1_year = now - relativedelta(years=1)
month_1=before_1_month.strftime('%Y-%m-%d')
month_3=before_3_month.strftime('%Y-%m-%d')
month_6=before_6_month.strftime('%Y-%m-%d')
month_12=before_1_year.strftime('%Y-%m-%d')


scores ={}
score_143850= 0
score_251350=0
score_195980=0
score_273130=0
score_305080=0
score_329750=0

for k , v in stocks.items():
 all = fdr.DataReader(str(k), before_1_year)
 month_1_df=all.truncate(after=month_1)
 month_3_df=all.truncate(after=month_3)
 month_6_df=all.truncate(after=month_6)
 month_12_df=all.truncate(before=month_12)
 
 today_close = all.tail(1).iloc[0].Close
 close_1 =month_1_df.tail(1).iloc[0].Close
 close_3 =month_3_df.tail(1).iloc[0].Close
 close_6 =month_6_df.tail(1).iloc[0].Close
 close_12 =month_12_df.head(1).iloc[0].Close
 
 rate_1= today_close / close_1 -1
 rate_3= today_close / close_3 -1
 rate_6= today_close / close_6 -1
 rate_12= today_close / close_12 -1
 #=(H9*12)+(J9*4)+(M9*2)+(S9*1)
 momentum_score = rate_1 * 12 + rate_3 *4 + rate_6 * 2 + rate_12
 scores[k] = momentum_score
 
 print(v + '현재가 ' + str(today_close) + "모멘텀 스코어 ="+str(momentum_score))

 
if score_143850 >= 0 and score_251350 >= 0 and score_195980 >=0  and score_273130 >= 0:
   result = max(score_143850 ,score_251350 , score_195980 ,score_273130 )
else:
   result = max(score_273130 , score_305080 , score_329750)
print(result)
 #print(v + '1 개월전 ' + str(month_1_df.tail(1)))
 #print(v + '3 개월전 ' + str(all.truncate(after=month_3)) )
 #print(v + '6 개월전 ' + str(all.truncate(after=month_6)) )
 #print(v + '6 개월전 ' + str(all.truncate(after=month_12)) )








