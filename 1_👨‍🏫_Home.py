import streamlit as st
import pandas as pd
import numpy as np
from streamlit_extras.app_logo import add_logo
import time

if "data" not in st.session_state:
    df = pd.read_csv("Companies.csv")
    #df = df.sort_values(by="Reach", ascending=False)
    st.session_state["data"] = df


# Configuração da página
st.set_page_config(page_title="Portifólio Eduardo Brites Coutinho", layout="wide")
st.sidebar.markdown("Desenvolvido por Eduardo Brites Coutinho [LinkedIn](https://www.linkedin.com/in/eduardo-brites-4b1332293/)")

col1, col2= st.columns([1, 3])

with col1:
    #st.markdown("<img src='img/D1/Home.png' style='widht: 100vw; display:flex; align-items: center; justify-content: center;'></img>", unsafe_allow_html=True)
    subcol1, subcol2, subcol3 = st.columns([2, 3, 2])
    with subcol2:
        st.image("img/Profile/me.jpg", use_container_width=True)
with col2:
    st.title("Eduardo Brites Coutinho")
    #st.markdown("<h1 style='text-align:center;'>Eduardo Brites Coutinho</h1>", unsafe_allow_html=True)
    
st.title("")

col1, col2, col3 = st.columns([1, 4, 1])

with col2:
    language = st.toggle(label="🌎")
    if language:
        text = "Hello! My name is Eduardo, and I am a programmer passionate about technology and innovation. I started my journey in high school, studying Systems Development, and I am currently studying at FIAP to become a Software Engineer. I have a constant desire to learn and improve my skills."
        
        text_list = text.split()
        text_space = st.empty()
        exibit = ""
    
        for x in text_list:
            exibit += x
            exibit += " "
            text_space.write(exibit)
            time.sleep(0.05)
        
        text = "I am a creative person, always looking for the best solutions to a given problem. Additionally, I am passionate about Design and constantly think about how proposed solutions can provide exceptional, unique, and accessible user experiences."

        text_list = text.split()
        text_space = st.empty()
        exibit = ""

        for word in text_list:
            exibit += word + " "
            text_space.write(exibit)
            time.sleep(0.05)
        
        text = "I have excellent communication and collaboration skills, absorbing and contributing with ideas and knowledge with my colleagues. I have extensive experience in Fullstack development and proficiency in core Front-End technologies such as HTML, CSS, and SASS. Currently, I am enhancing my skills as a Back-End developer, working with React, JavaScript, and Python."

        text_list = text.split()
        text_space = st.empty()
        exibit = ""

        for word in text_list:
            exibit += word + " "
            text_space.write(exibit)
            time.sleep(0.05)
    else:
        text = "Olá! Me chamo Eduardo e sou um programador apaixonado por tecnologia e inovação. Iniciei minha jornada no ensino médio, cursando Desenvolvimento de Sistemas, e atualmente estudo na FIAP para me tornar Engenheiro de Software. Tenho uma constante vontade de aprender e aprimorar minhas habilidades."
        
        text_list = text.split()
        text_space = st.empty()
        exibit = ""
    
        for x in text_list:
            exibit += x
            exibit += " "
            text_space.write(exibit)
            time.sleep(0.05)
        
        text = "Sou uma pessoa criativa, sempre buscando soluções adequadas para um mesmo problema. Além disso, sou apaixonado por Design e penso constantemente em como as soluções propostas podem proporcionar experiências excepcionais, únicas e acessíveis aos usuários."

        text_list = text.split()
        text_space = st.empty()
        exibit = ""

        for word in text_list:
            exibit += word + " "
            text_space.write(exibit)
            time.sleep(0.05)
        
        text = "Possuo excelentes habilidades de comunicação e colaboração, absorvendo e contribuindo com ideias e conhecimentos dos meus colegas. Tenho ampla experiência em desenvolvimento Fullstack e domínio das principais tecnologias de Front-End, como HTML, CSS e SASS. Atualmente, estou aprimorando minhas habilidades como desenvolvedor Back-End, utilizando React, JavaScript e Python."

        text_list = text.split()
        text_space = st.empty()
        exibit = ""

        for word in text_list:
            exibit += word + " "
            text_space.write(exibit)
            time.sleep(0.05)

st.title("")

"""col1, col2, col3, col4, col5 = st.columns([4, 3, 3, 3, 4])

with col2:
    subcol1, subcol2, subcol3 = st.columns([1, 10, 1])
    
    with subcol2:
        st.image("img/Contact/TELEPHONE.png", width=75, caption="(11) 98655-7073)")
        if st.button(label="Phone", type="primary"):
            st.success(body="(11)")
    
with col3:
    subcol1, subcol2, subcol3 = st.columns([1, 10, 1])
    
    with subcol2:
        st.image("img/Contact/MAIL.png", width=75, caption="eduardocoutinho30089@gmail.com")

with col4:
    subcol1, subcol2, subcol3 = st.columns([1, 10, 1])
    
    with subcol2:
        st.image("img/Contact/LINKEDIN.png", width=75, caption="Linkedin")"""