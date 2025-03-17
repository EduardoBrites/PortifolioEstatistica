import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Portifólio",
    page_icon="🎨",
    layout="wide"
)

st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho [LinkedIn](https://www.linkedin.com/in/eduardo-brites-4b1332293/)")

st.title("Portifólio", anchor=False)
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    
    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/D1/Home.png", caption="Project 1")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P1"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/yuYnNX549RSvflRu42VgpN/D1?node-id=0-1&t=UDioPVLitSXKbiuk-1)")
        st.write("")

        st.image("img/Biblioteca/Tela inicial.png", caption="Project 2")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P2"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/vtWxPHcI3t7kBreSGE1uqz/Untitled?t=UDioPVLitSXKbiuk-1)")
        
with col2:
    
    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/GS/Home_thumb.png", caption="Project 3")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P3"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/tsuAvwqgy3Rmgl05ziZ338/GS?t=UDioPVLitSXKbiuk-1)")
        st.write("")

        st.image("img/CPF/Frame 1.png", caption="Project 4")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P4"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/bs39Xj3dIHW553BG75bacc/Untitled?t=UDioPVLitSXKbiuk-1)")
        
with col3:

    subcol1, subcol2, subcol3 = st.columns([1, 6, 1])

    with subcol2:
        st.image("img/GS2/Home_thumb.png", caption="Project 5")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P5"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/WqcTOSUxBWndhMYPgryPQv/Untitled?t=UDioPVLitSXKbiuk-1)")
        st.write("")

        st.image("img/MEDEDUCA 1.0/Login.png", caption="Project 6")
        if st.button("Ver mais", type="secondary", use_container_width=True, key="P6"):
            st.write("[Clique aqui para ver o Figma](https://www.figma.com/design/CW3Hqf2jJQoBxIXmEwwclB/MEDEDUCA-1.0?t=UDioPVLitSXKbiuk-1)")