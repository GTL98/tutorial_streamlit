# --- Importar as bibliotecas --- #
from PIL import Image
import streamlit as st

# --- Criar o favicon --- #
favicon = Image.open('./imagens/favicon.png')

# --- Configuração da página --- #
st.set_page_config(
    page_title='Meu Site',
    page_icon=favicon,
    layout='wide'
)

# --- Inforação da página --- #
st.title('O parâmetro *layout* está como *wide*')
