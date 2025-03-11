import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo

if "data" not in st.session_state:
    df = pd.read_excel("Dados_InstagramCliente_AULA_3ESP.xlsx", index_col="Post ID")
    df = df.sort_values(by="Reach", ascending=False)
    st.session_state["data"] = df

# Configuração da página
st.set_page_config(page_title="Portifólio Eduardo Brites Coutinho", layout="wide")
st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho [LinkedIn](https://www.linkedin.com/in/eduardo-brites-4b1332293/)")

col1, col2= st.columns([1, 3])

with col1:
    #st.markdown("<img src='img/D1/Home.png', style:'widht: 100vw; display:flex; align-items: center; justify-content: center;'></img>", unsafe_allow_html=True)
    st.image("img/D1/Home.png", use_container_width=True)
with col2:
    st.title("Eduardo Brites Coutinho")


