#축제 시즌에 따른 축제역 지하철 인원 변동 분석
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform
import folium

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
festivaldata = pd.read_csv('festival.csv', encoding='cp949')
trainposition = pd.read_csv('position.csv', encoding='cp949')
positiondata= pd.DataFrame(trainposition)
mergedata = pd.merge(traindata, festivaldata, on="역명")

traingroup = mergedata.groupby(['역번호','날짜','호선','역명','구분','축제명','개최장소','축제시작일자','축제종료일자'])
trainfest = traingroup['합 계'].sum()
df=pd.DataFrame(trainfest)
df.to_csv('trainfest.csv', encoding='cp949')
df1= pd.read_csv('trainfest.csv', encoding='cp949')
df1.날짜 = pd.to_datetime(df1.날짜)
df1.축제시작일자 = pd.to_datetime(df1.축제시작일자)
df1.축제종료일자 = pd.to_datetime(df1.축제종료일자)
#print(df1)
#df2 -> 축제 기간동안 총합, df3 축제 기간외 총합
df2=df1.loc[(df1["날짜"] < df1["축제종료일자"])&(df1["날짜"]>df1["축제시작일자"]),["날짜","호선","역명","합 계","축제명","축제시작일자","축제종료일자"]]
df3=df1.loc[(df1["날짜"] > df1["축제종료일자"])|(df1["날짜"]<df1["축제시작일자"]),["날짜","호선","역명","합 계","축제명","축제시작일자","축제종료일자"]]
df2.날짜 = pd.to_datetime(df2.날짜)
df2=df2.set_index('날짜')
df3.날짜 = pd.to_datetime(df3.날짜)
df3=df3.set_index('날짜')
f1 = lambda x : round(x/x.sum()*100,2)
#print(df2.info) row = 422
#print(df3.info) row = 4246
festinum=df2.resample('A').mean()
intfest=int(festinum["합 계"])
nonfestinum=df3.resample('A').mean()
intnonfest=int(nonfestinum["합 계"])
sumnum = festinum+nonfestinum
#print("축제기간 비율",(festinum/sumnum)*100,"\n" "비축제기간 비율" ,(nonfestinum/sumnum)*100)
'''
#축제기간과 비축제기간에 따른 축제역 이용자수 원형그래프 시각화
people=[intfest, intnonfest]
labels=['festival','nonfesitlva']
plt.pie(people, labels=labels,autopct='%.2f%%')
plt.title("festival or Nonfestival")
plt.show()
'''

#축제역과 축제명 지도표시
df6=pd.DataFrame(positiondata)
festiposition = pd.merge(df1, df6, on=["역번호", "역명"])
df7=pd.DataFrame(festiposition)
df8=pd.DataFrame(df7[["역명","축제명","X좌표","Y좌표"]])
df9=df8.drop_duplicates()
print(df9)
trainmap = folium.Map(location = [37.553522, 126.986995], zoon_start = 12)

for data in df9.index:
    lat = df9.loc[data,"X좌표"]
    long = df9.loc[data,"Y좌표"]
    folium.CircleMarker([lat,long],radius=40,
                           popup = "역이름:"+df9.loc[data,"역명"]+"\n"+"축제명:"+df9.loc[data,"축제명"],
                           color = 'blue',
                           fill = True).add_to(trainmap)
trainmap.save('festmap.html')