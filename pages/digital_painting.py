import streamlit as st
st.set_page_config(
    page_title="대구광역시 미친개 이재학의 웹사이트",
    page_icon="🎨")

st.title("디지털 페인팅")

clp = "clip.png"
medi = "medi.png"

st.write("디지털 페인팅의 대표적인 특징은 기존의 아날로그 페인팅과는 달리 실수를 해도 쉽게 수정할 수 있다는 점 입니다.")
st.write("또한 레이어를 추가하여 초보자도 쉽게 채색을 할 수 있다는 점이 있으며")
st.write("굳이 비싼 재료를 사지 않아도 된다는 장점이 있습니다.")
st.write("그리고 3D 툴을 이용해 자세를 직접 잡을 수 있다는 장점이 있습니다")
st.image("info1.jpg")
st.caption("클립 스튜디오의 3d 툴")

st.divider()
st.subheader("무료")
button = st.button("메디방")
if button:
    st.image(medi)
    st.write("메디방 페인트는 저연령, 학생 계층에게 특히 인기가 많은 그래픽 페인팅 툴 입니다.")
    st.write("가장 큰 특징 중 하나는 :red[무료로] 모든 기능을 사용할 수 있는 것과 더불어")
    st.write("저사양 컴퓨터로도 웬만한 마지막 만찬같은 대형 그림이 아니면 잘 돌아간다는 특징이 있습니다.")
    st.write("그렇기에 무료 페인트 툴로써는 최고의 툴이라 할 수 있는 툴 입니다.")
    st.image("info.jpg")
    st.caption("메디방")
    if st.button("닫기"):
       st.write("뾰로롱")
if st.button("그림판"):
    st.image("hello.png")
    st.caption("금손이면 뭘해도 잘 합니다.")
    if st.button("닫기"):
       st.write("뾰로롱")


st.divider()
st.subheader("유료")
if st.button("클립 스튜디오"):
    st.image("clip.png")
    st.write("클립 스튜디오는 저렴한 가격에 불구하고도 전문적인 기능을 이용할 수 있으며 인터페이스도 직관적으로 설계되어 있어서 초보자들도 쉽게 할 수 있어서 초보자와 전문가 모두가 아주 쉽게 사용할 수 있는 프로그램입니다")
    st.write("그리고 소재를 공유하는 커뮤니티가 잘 활성화 되어 있어서 소재를 찾는데 어려움을 가지시는 분이라면 좋은 선택이 될 수 있습니다")
    st.write("https://assets.clip-studio.com/ko-kr")
    st.write("또한 궁금한 점을 사용자들끼리 묻고 답하는 공식 사이트도 있습니다")
    st.write("https://ask.clip-studio.com/ko-kr")
    st.image("Screenshot_20230909_094326_Chrome.jpg")
    st.image("Screenshot_20230909_094058_Clip Studio.jpg")
    st.write("그리고 제가 쓰는 툴이기도 합니다^^")
    st.image ("price.png")
    st.caption("근데 값을 달러로 매겨서 환율이 오르면 가격이 오르는 단점이 있습니다 ㅠㅠㅠ")
    st.subheader("")
    if st.button("닫기"):
        st.write("뾰로롱")

if st.button("포토샵"):
    st.image("photoshop.png")
    st.write("포토샵은 흔히 사진 합성이나 보정에 쓰이는 툴 이였습니다.")
    st.write("그런데 포토샵이 여러가지 필터와 보조기능이 많이 있는 툴이라서 디지털 페인팅 툴로 관심받게 됩니다.")
    st.image("11.webp")
    st.caption("출처-디자인베이스")
    st.image("photoshop12.webp")
    st.caption("출처-디자인베이스")
    st.write("그리고 만약 관련 직종을 가신다면 가장 많이 :red[보게될] 것이 될겁니다, 왜냐하면 요즘 회사에서는 제출 형식을 싸그리 포토샵 형식으로 내라 하거든요 클튜도 포토샵 파일을 지원하긴 하지만 파일이 손상되는 경우가 많아서...")
    st.write("그러나 취미 생활로 하실거라면 이 프로그램은 추천하지 않습니다")
    st.subheader("**월 2만4000원**")
    st.write("뭐... 대충 설명되죠?")
    if st.button("닫기"):
        st.write("뾰로롱")











