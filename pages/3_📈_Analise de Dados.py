import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Dados",
    page_icon="🏃🏼",
    layout="wide"
)

df = st.session_state["data"]

st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho")

df
st.write(df.describe())