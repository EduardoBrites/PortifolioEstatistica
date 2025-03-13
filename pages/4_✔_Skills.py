import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Skills",
    page_icon="🏃🏼",
    layout="wide"
)

st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho")

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

col1, col2, col3, col4, col5 = st.columns([1, 3, 3, 3, 1])

with col2:
    st.write("a")

with col3:
    st.write("b")

with col4:
    st.write("c")