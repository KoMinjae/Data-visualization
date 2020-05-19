#지하철 역별 이용자수
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
traingroup = traindata.groupby(['날짜','호선', '역번호', '역명'])
trainsum = traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('traintimesum.csv', encoding='cp949')
df1= pd.read_csv('traintimesum.csv', encoding='cp949')
df1.날짜 = pd.to_datetime(df1.날짜)
df1 = df1.set_index('날짜')
hosun=[]
for i in range(0,8):
    strhosun = str(i+1)+"호선"
    strhosun = str(i + 1) + "호선"
    df2 = df1.loc[df1['호선'] == strhosun,["역명","합 계"]]

    #역별 이용자수 평균 막대 그래프
    df2.groupby("역명").mean().plot(kind='bar')
    plt.show()


    #역별 이용자수 평균 원형 그래프
    df3=df2.groupby("역명").mean()
    del df3["합 계"]
    plt.pie(df2.groupby("역명").mean(),labels=df3.index,autopct='%.2f%%')
    plt.show()




