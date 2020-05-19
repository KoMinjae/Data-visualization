#요일별 탑승 인원 비율 분석
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
traingroup = traindata.groupby(['날짜','호선','구분'])
trainsum = traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('traintimesum.csv', encoding='cp949')
df1= pd.read_csv('traintimesum.csv', encoding='cp949')
df1.날짜 = pd.to_datetime(df1.날짜)
df1['요일']=df1['날짜'].dt.weekday_name
df1 = df1.set_index('날짜')
f1= lambda x : round(x/x.sum()*100,2)
for i in range(0,8):
    strhosun = str(i + 1) + "호선"
    df2=df1.loc[df1['호선']==strhosun,["호선","구분","요일","합 계"]]
    #print(strhosun,"호선 요일별 분석",df2.groupby("요일").sum().apply(f1,axis=0))
    #호선별 요일별 이용자 막대그래프 시각화
    #df2.groupby("요일").sum().apply(f1,axis=0).plot(kind='bar')
    #plt.title('No.%i' % (i + 1))
    #plt.show()
    # 호선별 요일별 이용자 원형그래프 시각화
    labels=['Friday','Monday','Saturday','Sunday','Thursday','Tuesday','Wednesday']
    plt.pie(df2.groupby("요일").sum().apply(f1, axis=0), labels=labels,autopct='%.2f%%')
    plt.title('No.%i' % (i + 1))
    plt.show()