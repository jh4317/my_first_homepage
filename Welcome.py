import streamlit as st
import os
import matplotlib.font)manager as fm
font_dirs = [os.getcwd() + '/customFonts']
font_files = fm.findSystemFonts(fontpaths=font_dirs)

for font_file in font_files:
    fm.fontManager.addfont(font_file)
fm._load_fontmanager(try_read_cache=False)


st.title("이재학의 미술시간😎😋")
st.image("20230908_215055.jpg")
st.image("20230829_150336.jpg")
