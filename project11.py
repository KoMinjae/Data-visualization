#호선별 이용자수 히스토그램
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
traingroup = traindata.groupby(['날짜','호선',])
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
    df2 = df1.loc[df1['호선'] == strhosun,["합 계"]]
    df2.plot(kind="hist",)
    plt.show()