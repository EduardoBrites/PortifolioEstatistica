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

# Adicionando logo com streamlit-extras
# add_logo("logo.jpeg")

# Adicionando o logo
st.logo("logo.png")

# Adicionando o logo no body
st.image("logo.png", width=150)

st.html(
    "<h1>Eduardo Brites Coutinho</h1>"
)


