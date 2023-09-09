import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
cat = "cat.jpg"

st.image(cat)
options = st.multiselect(
'당신의 특성은?',
['미술관련 종사자', '학생', '백수', '뭐고'],
['뭐고'])


st.write(f'당신의 선택은: :red[{options}] 입니다.')
if options== ["미술관련 종사자"]:
    st.write("당신에게는 어도비 포토샵이 좋겠네요!")
    st.write("https://www.adobe.com/creativecloud/business-plans.html?plan=team&step=2&promoid=49F59P92&mv=other")
elif options == ["학생"]:
    st.write("메디방으로 흥미를 가져보시고 재미있으시면 클립 스튜디오를 써보시는게 어떨까요?")
    st.write("https://medibangpaint.com/ko/app-download/")
    st.caption("메디방")
    st.write("https://www.clipstudio.net/kr/purchase/")
    st.caption("클립 스튜디오")
elif options == ["백수"]:
    st.header("그림 그리지 말고 직업을 가지시는건 어떨까요????😋")
    st.write("https://www.jobkorea.co.kr")
elif options == ["백수", "학생"]:
    st.write("학생이 백수가 맞긴 하죠...? 그림판 쓰실래요?")
elif options == ["미술관련 종사자", "학생"]:
    st.write("꿈이 미술관련 종사자이신 학생이시군요! 주변 친구들에게 '와 너 그림 진짜 잘그린다' 라는 소리 못 들으시면 공부가 더 편할수도 있어요!")
    st.write("https://namu.wiki/w/%EC%9E%85%EC%8B%9C%EB%AF%B8%EC%88%A0")
elif options == ['미술관련 종사자', '학생', '백수', '뭐고']:
    st.title("좀😋😋😋😋😋")
elif options == ['학생', '백수', '뭐고']:
    st.title("좀😋😋")
elif options == ['미술관련 종사자', '백수', '뭐고']:
    st.title("좀😋🥵🥵🥵🥵🥶🥶😧🥶🥶")
else:
    st.subheader("뭐고")




