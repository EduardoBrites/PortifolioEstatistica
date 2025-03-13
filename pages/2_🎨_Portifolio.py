import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Portifólio",
    page_icon="🏃🏼",
    layout="wide"
)

st.title("Portifólio", anchor=False)
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    
    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/D1/Home.png", caption="Project 1")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P1"):
            st.write("Project 1")
        st.write("")

        st.image("img/Biblioteca/Tela inicial.png", caption="Project 2")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P2"):
            st.write("Project 2")
        
with col2:
    
    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/GS/Home_thumb.png", caption="Project 3")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P3"):
            st.write("Project 3")
        st.write("")

        st.image("img/CPF/Frame 1.png", caption="Project 4")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P4"):
            st.write("Project 4")
        
with col3:

    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/GS2/Home_thumb.png", caption="Project 5")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P5"):
            st.write("Project 5")
        st.write("")

        st.image("img/MEDEDUCA 1.0/Login.png", caption="Project 6")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P6"):
            st.write("Project 6")