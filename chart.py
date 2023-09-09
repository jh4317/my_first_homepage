import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import  rc, font_manager
import numpy as np
st.title(":green[이재학의 실험방]")

data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})
st.dataframe(data, use_container_width=True)

font_path = "C:\WINDOWS\FONTS\BATANG.TTC"
font = font_manager.FontProperties(fname=font_path).get_name()
plt.rc('font', family=font)

fig1,ax =plt.subplots()
ax.bar(data['이름'], data['나이'])
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                (p.get_x() +p.get_width()/ 2., p.get_height()),
                ha= 'center', va = 'center',
                xytext = (0, 15),
                textcoords = 'offset points')
ax.set_ylim(0, 40)
st.pyplot(fig1)

path= '인.csv'
data1 = pd.read_csv(path, encoding='cp949')
print(data1)
st.dataframe(data1, use_container_width=True)

fig3, ax = plt.subplots()
plt.title('출생아 수 추이')
ax.bar(data1['시점'], data1['출생아수(명)'])
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")
for p in ax.patches:
    ax.annotate(format(p.get_height(), '.1f'),
                (p.get_x() +p.get_width()/ 2., p.get_height()),
                ha= 'center', va = 'center',
                xytext = (0, 15),
                textcoords = 'offset points')
ax.set_ylim(200000, 500000)
st.pyplot(fig3)

fig4, ax = plt.subplots()
plt.title('출생아 수 추이')
ax.plot(data1['시점'], data1['출생아수(명)'], color="#ADFF2F", marker="8", linestyle="--")
plt.xlabel("연도")
plt.ylabel("출생아수(단위: 명)")

for i, txt in enumerate(data1['출생아수(명)']):
    ax.text(data1['시점'][i], txt, str(txt), ha='center', va='bottom')
ax.set_ylim(200000, 500000)
st.pyplot(fig4)



#justice what's the right thing to do