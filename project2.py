#호선별 기온과 지하철 승차인원 상관관계 분석
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.anova import anova_lm
import numpy as np
import scipy.stats as ss
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
tempdata = pd.read_csv('tempdata.csv')
gangnam = tempdata.loc[tempdata['지점명']=='강남',['날짜','평균기온',]]
gangnam.날짜 = pd.to_datetime(gangnam.날짜)
gangnam = gangnam.set_index('날짜')
#강남지역 월 평균 기온 막대그래프
#gangnam.resample('M').mean().plot(kind='bar')
#plt.show()
#1호선 : 용산, 2호선 : 강남, 3호선 : 광진, 4호선 : 동작, 5호선 : 강동, 6호선 : 남산, 7호선 : 동작, 8호선 : 송파
temp=[]
temp.append(tempdata.loc[tempdata['지점명']=='용산',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='강남',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='광진',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='동작',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='강동',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='남산',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='동작',['날짜','평균기온','평균습도','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='송파',['날짜','평균기온','평균습도','강수량']])
#강남지역 평균기온 히스토그램
temphist = temp[1]["평균기온"]
temphist.plot(kind="hist")
plt.show()
mergedata=[]
for i in temp:
    mergedata.append(pd.merge(traindata, i, on = '날짜'))
hosun=[]
for i in range(0,8):
    traingroup = mergedata[i].groupby(['날짜','호선','평균기온','평균습도','강수량'])
    traintemp=traingroup['합 계'].sum()
    df=pd.DataFrame(traintemp)
    df.to_csv('traintemp.csv', encoding='cp949')
    df2=pd.read_csv('traintemp.csv',encoding='cp949')
    df1=pd.DataFrame(df2)
    df1['합계']=df1['합 계'].astype(float)
    strhosun = str(i+1)+"호선"
    hosun.append(df1.loc[df1['호선']==strhosun,['날짜','호선','합 계','합계','평균기온']])
#hosun1=df1.loc[df1['호선']=='1호선',['날짜','호선','합 계','평균기온']]
'''
#기온, 지하철인원이용 Linear Regression 분석
model = smf.ols(formula='합계~평균기온', data=hosun[0])
result = model.fit()
print(result.summary())
'''
#기온, 지하철 이용객수 ANOVA분석
anovadf= df1[['호선','합계','평균기온']]
for name_group in df1.groupby('호선'):
    samples = [avgtemp[1] for avgtemp in name_group[1].groupby('평균기온')['합계']]
    f_val, p_val = ss.f_oneway(*samples)
    print('호선: {}, F value: {:.3f}, p value: {:.3f}'.format(name_group[0], f_val, p_val))


#for i in range(0,8):

    #print(i+1,"호선",hosun[i].corr())
    # 기온과 이용자수 히트맵 시각화
    #plt.matshow((hosun[i].corr()))
    #plt.show()
    # 호선별 기온, 이용자수 합계 산점도 시각화
    #plt.scatter(hosun[i]['합 계'], hosun[i]['평균기온'])
    #plt.title('No.%i'%(i+1))
    #plt.show()
