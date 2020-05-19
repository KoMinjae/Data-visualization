#지도를 사용한 데이터 시각화
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
import folium

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
trainposition = pd.read_csv('position.csv', encoding='cp949')
positiondata= pd.DataFrame(trainposition)


#호선, 날짜 입력받아서 해당 지하철 이용수 나타내기
del positiondata["역명"]
del positiondata["호선"]
mergedata = pd.merge(traindata, positiondata, on = "역번호")
hosun=[]
for i in range(0,8):
    strhosun = str(i+1)+"호선"
    hosun.append(mergedata.loc[mergedata['호선']==strhosun,['날짜','호선','역명','합 계','X좌표','Y좌표']])
#초기위치 설정
trainmap = folium.Map(location = [37.553522, 126.986995], zoon_start = 12)
number = int(input("호선을 입력하세요"))
date=input("날짜를 입력하세요(2019-01-01~2019-06-30")

df2=hosun[number-1].loc[hosun[number-1]['날짜']==date,['역명','합 계','X좌표','Y좌표']]
for data in df2.index:
    lat = df2.loc[data,"X좌표"]
    long = df2.loc[data,"Y좌표"]
    folium.CircleMarker([lat,long],radius=df2.loc[data,"합 계"]/1500,
                           popup = df2.loc[data,"역명"]+str(df2.loc[data,"합 계"]),
                           color = 'blue',
                           fill = True).add_to(trainmap)
trainmap.save('hosundatemap.html')

'''
#상위 5개 이용역 지도 표시
df1=traindata.groupby(["호선", "역번호", "역명"])
trainsum=(df1["합 계"].sum())
df2=pd.DataFrame(trainsum)
traintop5=df2.sort_values(by=["합 계"], ascending=False).head()
mergetop5=pd.merge(traintop5, positiondata, on=["역번호","호선"])
df3=pd.DataFrame(mergetop5)
df3.drop_duplicates()
print(df3.drop_duplicates())
trainmap = folium.Map(location = [37.553522, 126.986995], zoon_start = 12)
for data in df3.index:
    lat = df3.loc[data,"X좌표"]
    long= df3.loc[data,"Y좌표"]
    folium.CircleMarker([lat,long],radius=df3.loc[data,"합 계"]/700000,
                           popup = df3.loc[data,"호선"]+df3.loc[data,"역명"]+str(df3.loc[data,"합 계"]),
                           color = 'blue',
                           fill = True).add_to(trainmap)
trainmap.save('5topmap.html')
'''
'''
#하위 5개 이용역 지도 표시
df1=traindata.groupby(["호선", "역번호", "역명"])
trainsum=(df1["합 계"].sum())
df2=pd.DataFrame(trainsum)
traintop5=df2.sort_values(by=["합 계"], ascending=True).head()
mergetop5=pd.merge(traintop5, positiondata, on=["역번호","호선"])
df3=pd.DataFrame(mergetop5)
df3.drop_duplicates()
print(df3.drop_duplicates())
trainmap = folium.Map(location = [37.553522, 126.986995], zoon_start = 12)
for data in df3.index:
    lat = df3.loc[data,"X좌표"]
    long= df3.loc[data,"Y좌표"]
    folium.CircleMarker([lat,long],radius=df3.loc[data,"합 계"]/20000,
                           popup = df3.loc[data,"호선"]+df3.loc[data,"역명"]+str(df3.loc[data,"합 계"]),
                           color = 'blue',
                           fill = True).add_to(trainmap)
trainmap.save('5bottommap.html')
'''