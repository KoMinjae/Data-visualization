#매월 시간대별 지하철 탑승 인원 비율 분석

import pandas as pd
import matplotlib.pyplot as plt
from pyculiarity import detect_ts
from pyculiarity.date_utils import date_format
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
traingroup = traindata.groupby(['날짜','호선','구분','05 ~ 06','06 ~ 07','07 ~ 08','08 ~ 09','09 ~ 10','10 ~ 11','11 ~ 12','12 ~ 13','13 ~ 14','14 ~ 15','15 ~ 16','16 ~ 17','17 ~ 18','18 ~ 19','19 ~ 20','20 ~ 21','21 ~ 22','22 ~ 23','23 ~ 24','00 ~ 01'])
trainsum = traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('traintimesum.csv', encoding='cp949')
df1= pd.read_csv('traintimesum.csv', encoding='cp949')
df1.날짜 = pd.to_datetime(df1.날짜)
df1 = df1.set_index('날짜')
df1['합계']=df1['합 계'].astype(float)
df3=df1.loc[df1['호선']=='1호선',['합계']]
f1= lambda x : round(x/x.sum()*100,2)
for i in range(0,8):
    strhosun = str(i + 1) + "호선"
    df2=df1.loc[df1['호선']==strhosun,["호선","구분",'05 ~ 06','06 ~ 07','07 ~ 08','08 ~ 09','09 ~ 10','10 ~ 11','11 ~ 12','12 ~ 13','13 ~ 14','14 ~ 15','15 ~ 16','16 ~ 17','17 ~ 18','18 ~ 19','19 ~ 20','20 ~ 21','21 ~ 22','22 ~ 23','23 ~ 24','00 ~ 01']].resample('M').sum().apply(f1,axis=1)

    #print(strhosun)
    #print(df2)
    #호선별 시간대별 이용자 원형그래프 시각화
    #time=['05 ~ 06','06 ~ 07','07 ~ 08','08 ~ 09','09 ~ 10','10 ~ 11','11 ~ 12','12 ~ 13','13 ~ 14','14 ~ 15','15 ~ 16','16 ~ 17','17 ~ 18','18 ~ 19','19 ~ 20','20 ~ 21','21 ~ 22','22 ~ 23','23 ~ 24','00 ~ 01']
    #labels=list(time)
    #plt.pie(df1.loc[df1['호선']==strhosun,["호선","구분",'05 ~ 06','06 ~ 07','07 ~ 08','08 ~ 09','09 ~ 10','10 ~ 11','11 ~ 12','12 ~ 13','13 ~ 14','14 ~ 15','15 ~ 16','16 ~ 17','17 ~ 18','18 ~ 19','19 ~ 20','20 ~ 21','21 ~ 22','22 ~ 23','23 ~ 24','00 ~ 01']].resample('A').sum().apply(f1,axis=1),labels=labels, autopct='%.2f%%')
    #plt.show()

    #월별 호선별 시간대별 이용자 막대그래프 시각화
    #df2.plot(kind='bar')
    #plt.legend(loc=1)
    #plt.show()
