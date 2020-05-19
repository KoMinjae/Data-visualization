#호선별 일별 이용자수 ARIMA 분석
import pandas as pd
import matplotlib.pyplot as plt
from pyculiarity import detect_ts
from pyculiarity.date_utils import date_format
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.arima_model import ARIMA
import matplotlib
from matplotlib import font_manager, rc
import platform

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

traindata = pd.read_csv('traindata.csv', encoding='cp949')
traingroup = traindata.groupby(['날짜','호선'])
trainsum = traingroup['합 계'].sum()
df=pd.DataFrame(trainsum)
df.to_csv('traintimesum.csv', encoding='cp949')
df1= pd.read_csv('traintimesum.csv', encoding='cp949')
df1.날짜 = pd.to_datetime(df1.날짜)
df1 = df1.set_index('날짜')
df1['합계']=df1['합 계'].astype(float)
del df1['합 계']
df3=df1.loc[df1['호선']=='1호선',['합계']]
#plot_pacf(df3)
#plot_acf(df3)
#plt.show()

#ARIMA 분석
model = ARIMA(df3, order=(1,1,0))
model_fit = model.fit(trend='nc',full_output=True, disp=1)
print(model_fit.summary())
model_fit.plot_predict()
plt.show()
fore=model_fit.forecast(steps=1)
print(fore)



#월별 지하철 총 이용자수 평균 막대그래프
df1.resample('M').mean().plot(kind='bar')
plt.show()



#월별 지하철 이용자수 평균 꺽은선 그래프
df1.resample('M').mean().plot()
plt.show()

