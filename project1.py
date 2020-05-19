#기름값과 지하철 이용 고객수 상관관계 분석
import pandas as pd
import csv
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.linear_model import LinearRegression
import scipy.stats as ss
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv',encoding='cp949')
oildata = pd.read_csv('oildata.csv',encoding='cp949')

#서울, 경기도 기름값 월 변화 꺽은선그래프
oildata.날짜 = pd.to_datetime(oildata.날짜)
oildata = oildata.set_index('날짜')
oildata.resample('M').mean().plot()
plt.show()

#서울, 경기도 기름값 히스토그램
oildata.plot(kind='hist',alpha=0.5)
plt.show()
mergedata=pd.merge(traindata,oildata,on="날짜")
traingroup = mergedata.groupby(['날짜','호선','구분','경기','서울'])
trainsum=traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('trainsum.csv', encoding='cp949')
df1=pd.read_csv('trainsum.csv', encoding='cp949')
df=pd.DataFrame(df1)
df['합계']=df["합 계"].astype(np.float)
print(df.dtypes)
hosun=[]
hosun.append(df.loc[df["호선"]=="1호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="2호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="3호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="4호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="5호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="6호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="7호선",["날짜","호선","합계","경기","서울"]])
hosun.append(df.loc[df["호선"]=="8호선",["날짜","호선","합계","경기","서울"]])

'''
#Linear Regression 분석
model = smf.ols(formula= "합계 ~ 서울", data = hosun[0])
result = model.fit()
print(result.summary())
'''

#기름값 지하철 이용자수 ANOVA분석
anovadf= df[['호선','합계','서울']]
for name_group in df1.groupby('호선'):
    samples = [avgtemp[1] for avgtemp in name_group[1].groupby('서울')['합계']]
    f_val, p_val = ss.f_oneway(*samples)
    print('호선: {}, F value: {:.3f}, p value: {:.3f}'.format(name_group[0], f_val, p_val))

#for i in hosun:
 #print(i.corr())
 #기름값과 이용자수 시각화
 #plt.matshow(i.corr())
 #plt.show()
