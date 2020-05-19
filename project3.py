#미세먼지, 지하철 이용 객수 상관관계 분석

import pandas as pd
import csv
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
dustdata = pd.read_csv('dustdata.csv')
#1호선 : 영등포구, 2호선 : 강남구, 3호선 : 광진구, 4호선 : 동작구, 5호선 : 강동구, 6호선 : 남산, 7호선 : 동작구, 8호선 : 송파구
dust=[]
dust.append(dustdata.loc[dustdata['측정소명']=='영등포구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='강남구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='광진구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='동작구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='강동구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='남산',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='동작구',['날짜','미세먼지','초미세먼지']])
dust.append(dustdata.loc[dustdata['측정소명']=='송파구',['날짜','미세먼지','초미세먼지']])
#강남지역 미세먼지, 초미세먼지 히스토그램
dust[1].plot(kind='hist', alpha=0.5)
plt.show()
mergedata=[]
for i in dust:
    mergedata.append(pd.merge(traindata, i, on = '날짜'))
hosun=[]
for i in range(0,8):
    traingroup = mergedata[i].groupby(['날짜','호선','구분','미세먼지','초미세먼지'])
    dusttemp=traingroup['합 계'].sum()
    df=pd.DataFrame(dusttemp)
    df.to_csv('traindust.csv', encoding='cp949')
    df2=pd.read_csv('traindust.csv',encoding='cp949')
    df1=pd.DataFrame(df2)
    df1['합계']=df1['합 계'].astype(float)
    strhosun = str(i+1)+"호선"
    hosun.append(df1.loc[df1['호선']==strhosun,['날짜','호선','합계','합 계','미세먼지','초미세먼지']])

#미세먼지, 초미세먼지, 지하철인원이용 Linear Regression 분석
model = smf.ols(formula='합계~미세먼지+초미세먼지', data=hosun[0])
result = model.fit()
print(result.summary())

for i in range(0,8):
    print(i+1,"호선",hosun[i].corr())
    #미세먼지,초미세먼지와 이용자수 시각화
    #plt.matshow(hosun[i].corr())
    #plt.show()
    # 호선별 미세먼지, 이용자수 합계 산점도 시각화
    #plt.scatter(hosun[i]['합 계'], hosun[i]['미세먼지'])
    #plt.title('No.%i'%(i+1))
    #plt.show()
    # 호선별 초미세먼지, 이용자수 합계 산점도 시각화
    plt.scatter(hosun[i]['합 계'], hosun[i]['미세먼지'])
    plt.title('No.%i'%(i+1))
    plt.show()
