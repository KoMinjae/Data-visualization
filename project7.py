#눈, 비의 유무에 따른 승차 인원 비교
import pandas as pd
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
tempdata = pd.read_csv('tempdata.csv')

#강남지역 월별 총 강수량 막대그래프 시각화
howrain = tempdata.loc[tempdata['지점명']=='강남',['날짜','강수량',]]
howrain.날짜 = pd.to_datetime(howrain.날짜)
howrain = howrain.set_index('날짜')
#강남지역 강수,강우량 히스토그램
howrain.plot(kind='hist')
plt.show()
#print(howrain.resample('M').sum())
#강남지역 월별 강수,강우 누적량
#howrain.resample('M').sum().plot(kind='bar')
#plt.show()
#1호선 : 용산, 2호선 : 강남, 3호선 : 광진, 4호선 : 동작, 5호선 : 강동, 6호선 : 남산, 7호선 : 동작, 8호선 : 송파
temp=[]
temp.append(tempdata.loc[tempdata['지점명']=='용산',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='강남',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='광진',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='동작',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='강동',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='남산',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='동작',['날짜','강수량']])
temp.append(tempdata.loc[tempdata['지점명']=='송파',['날짜','강수량']])
mergedata=[]
for i in temp:
    mergedata.append(pd.merge(traindata, i, on = '날짜'))
hosun=[]
rainhosun=[]
notrainhosun=[]
for i in range(0,8):
    traingroup = mergedata[i].groupby(['날짜','호선','구분','강수량'])
    traintemp=traingroup['합 계'].sum()
    df=pd.DataFrame(traintemp)
    df.to_csv('traintemp.csv', encoding='cp949')
    df2=pd.read_csv('traintemp.csv',encoding='cp949')
    df1=pd.DataFrame(df2)
    df1['합계']=df1['합 계'].astype(float)
    strhosun = str(i+1)+"호선"
    hosun.append(df1.loc[(df1['호선']==strhosun),['날짜','호선','합계','합 계','강수량']])
    rainhosun.append(df1.loc[(df1['호선']==strhosun)&(df1['강수량']!=0.0),['날짜','호선','합계','합 계','강수량']])
    notrainhosun.append(df1.loc[(df1['호선']==strhosun)&(df1['강수량']==0.0),['날짜','호선','합계','합 계','강수량']])
#미세먼지, 강수량 Linear Regression 분석
model = smf.ols(formula='합계~강수량', data=hosun[0])
result = model.fit()
print(result.summary())
'''
#for i in range(0,8):
    #print(i+1,"호선",hosun[i].corr())
    #print(i+1,"호선 비율",((rainhosun[i]['합 계'].sum()/len(rainhosun[i]))/((rainhosun[i]['합 계'].sum()/len(rainhosun[i]))+(notrainhosun[i]['합 계'].sum()/len(notrainhosun[i]))))*100, ((notrainhosun[i]['합 계'].sum()/len(notrainhosun[i]))/((rainhosun[i]['합 계'].sum()/len(rainhosun[i]))+(notrainhosun[i]['합 계'].sum()/len(notrainhosun[i]))))*100)
    #plt.matshow(hosun[i].corr())
    #plt.show()
    #강수량에 따른 호선별 지하철 이용 인원 원형 그래프 시각화
    rainpeople = rainhosun[i]['합 계'].mean()
    notrainpeople = notrainhosun[i]['합 계'].mean()
    people=[rainpeople,notrainpeople]
    labels=['rain','notrain']
    plt.pie(people, labels=labels, autopct='%.2f%%')
    plt.show()
'''