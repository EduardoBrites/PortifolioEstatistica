import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Skills",
    page_icon="❇️",
    layout="wide"
)

st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho [LinkedIn](https://www.linkedin.com/in/eduardo-brites-4b1332293/)")

col1, col2 = st.columns([1, 4])

with col1:
    subcol1, subcol2, subcol3 = st.columns([1, 2, 1])

    with subcol2:
        st.image("img/svg/list-check.svg", use_container_width=True)

with col2:
    st.title("Skills", anchor=False)

st.write("")
st.write("")
st.write("")

col1, col2, col3, col4, col5, col6, col7 = st.columns([1, 3, 3, 3, 3, 3, 1])

with col2:
    subcol1, subcol2, subcol3 = st.columns([1, 3, 1])
    
    with subcol2:
        st.image("img/Skills/HTML5.png", width=75, caption="HTML")
        st.write("")
        st.image("img/Skills/SASS.png", width=75, caption="SASS")
        st.write("")
        st.image("img/Skills/PHOTOSHOP.png", width=75, caption="PHOTOSHOP")
    
with col3:
    subcol1, subcol2, subcol3 = st.columns([1, 3, 1])
    
    with subcol2:
        st.image("img/Skills/CSS3.png", width=75, caption="CSS")
        st.write("")
        st.image("img/Skills/FIGMA.png", width=75, caption="FIGMA")
        st.write("")
        st.image("img/Skills/ILLUSTRATOR.png", width=75, caption="ILLUSTRATOR")

with col4:
    subcol1, subcol2, subcol3 = st.columns([1, 3, 1])
    
    with subcol2:
        st.image("img/Skills/JAVASCRIPT.png", width=75, caption="JAVA SCRIPT")
        st.image("img/Skills/GIT.png", width=75, caption="GIT")
        st.image("img/Skills/VISUALBASIC.png", width=75, caption="VISUAL BASIC")

with col5:
    subcol1, subcol2, subcol3 = st.columns([1, 3, 1])
    
    with subcol2:
        st.image("img/Skills/REACT.png", width=75, caption="REACT")
        st.write("")
        st.image("img/Skills/SQL.png", width=75, caption="SQL")
        st.write("")
        st.image("img/Skills/PYTHON.png", width=75, caption="PYTHON")

with col6:
    subcol1, subcol2, subcol3 = st.columns([1, 3, 1])
    
    with subcol2:
        st.image("img/Skills/NODEJS.png", width=75, caption="NODE.JS")
        st.write("")
        st.image("img/Skills/JAVA.png", width=75, caption="JAVA")
        st.write("")
        st.image("img/Skills/CPP.png", width=75, caption="C++")