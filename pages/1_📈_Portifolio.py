import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="Portifólio",
    page_icon="🏃🏼",
    layout="wide"
)

def crop_image(path):
    im = Image.open(path)
    
    width, height = im.size
    
    bottom = 3*height / 4
    
    im1 = im.crop((0, 0, 0, bottom))
    return im1 

st.title("Portifólio", anchor=False)

col1, col2, col3 = st.columns(3)

with col1:
    
    st.image("img/D1/Home.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P1"):
        st.write("Project 1")
    st.write("")
    
    st.image("img/Biblioteca/Tela inicial.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P2"):
        st.write("Project 1")
        
with col2:
    
    image1 = crop_image("img/GS2/Home.png")
    st.image("img/GS2/Home.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P3"):
        st.write("Project 1")
    st.write("")
    
    st.image("img/Biblioteca/Tela inicial.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P4"):
        st.write("Project 1")
        
with col3:
    st.image("img/D1/Home.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P5"):
        st.write("Project 1")
    st.write("")
    
    st.image("img/Biblioteca/Tela inicial.png", caption="Project 1")
    if st.button("Ver mais", type="secondary", use_container_width=True, key="P6"):
        st.write("Project 1")