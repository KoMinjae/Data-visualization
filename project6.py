#학기, 비학기 시즌에 따른 대학가역 지하철 인원 변동 분석
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False
traindata = pd.read_csv('traindata.csv', encoding='cp949')
#청량리(서울시립대입구), 한양대, 건대입구, 교대(법원,검찰청),
#낙성대, 서울대입구(관악구청), 이대, 한성대입구(삼선교)
#숙대입구(갈월), 고려대(종암), 숭실대입구(살피재), 신촌,길음,수유(강북구청)
#혜화,총신대입구(이수),공릉(서울과학기술대)
traingroup = traindata.groupby(['날짜','호선','역명','구분'])
trainsum=traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('trainsum.csv', encoding='cp949')
df1 = pd.read_csv('trainsum.csv', encoding='cp949')

hosun1=df1.loc[(df1['역명']=="청량리(서울시립대입구)")|(df1['역명']=="신촌")|(df1['역명']=="공릉(서울과학기술대)")|(df1['역명']=="총신대입구(이수)")|(df1['역명']=="길음")|(df1['역명']=="수유(강북구청")|(df1['역명']=="혜화")|(df1['역명']=="한양대")|(df1['역명']=="건대입구")|(df1['역명']=="교대(법원.검찰청)")|(df1['역명']=="낙성대")|(df1['역명']=="서울대입구(관악구청)")|(df1['역명']=="이대")|(df1['역명']=="한성대입구(삼선교)")|(df1['역명']=="숙대입구(갈월)")|(df1['역명']=="고려대(종암)")|(df1['역명']=="숭실대입구(살피재)"),["날짜","호선","역명","합 계"]]
hosun1.날짜 = pd.to_datetime(hosun1.날짜)
hosun1 = hosun1.set_index('날짜')
hosun2=df1.loc[(df1['역명']!="청량리(서울시립대입구)")&(df1['역명']!="신촌")&(df1['역명']!="공릉(서울과학기술대)")&(df1['역명']!="총신대입구(이수)")&(df1['역명']!="길음")&(df1['역명']!="수유(강북구청")&(df1['역명']!="혜화")&(df1['역명']!="한양대")&(df1['역명']!="건대입구")&(df1['역명']!="교대(법원.검찰청)")&(df1['역명']!="낙성대")&(df1['역명']!="서울대입구(관악구청)")&(df1['역명']!="이대")&(df1['역명']!="한성대입구(삼선교)")&(df1['역명']!="숙대입구(갈월)")&(df1['역명']!="고려대(종암)")&(df1['역명']!="숭실대입구(살피재)"),["날짜","호선","역명","합 계"]]

hosun2.날짜 = pd.to_datetime(hosun2.날짜)
hosun2=hosun2.set_index('날짜')
f1 = lambda x : round(x/x.sum()*100,2)
print("대학역", hosun1.resample('M').sum().apply(f1,axis=0))
print("비 대학역", hosun2.resample('M').sum().apply(f1,axis=0))
labels = ["1M","2M","3M","4M","5M","6M"]
#대학가역 1~6월 원형그래프 시각화
#plt.pie(hosun1.resample('M').sum().apply(f1,axis=0), labels=labels, autopct='%.2f%%')
#plt.title("University")
#plt.show()
#비 대학가역 1~6월 원형그래프 시각화
plt.pie(hosun2.resample('M').sum().apply(f1,axis=0), labels=labels, autopct='%.2f%%')
plt.title("NotUniversity")
plt.show()