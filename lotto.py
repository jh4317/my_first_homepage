import streamlit as st
import random
import datetime

st.title("일등은 나의 것👩🏿‍🦱")

button = st. button ('asjdjhfklasjdfk')

if button:
    for i in range(1, 6):
        lotto =set()
        while len(lotto)<6:
            number = random.randint(1, 46)
            lotto.add(number)
        lotto= list(lotto)
        lotto.sort()
        st.subheader(f'{i}. 행운의 번호: :green[{lotto}]')
    st.write("로또 번호 생성된 시각: ", datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))