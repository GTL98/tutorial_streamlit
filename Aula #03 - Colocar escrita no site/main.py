# --- Importar a biblioteca --- #
import streamlit as st

# --- Adicionar um título --- #
st.title('Isso aqui é um título. Podemos colocar :green[cor] e emojis :sunglasses:!')

# --- Adicionar uma header --- #
st.header(
    'Isso aqui é uma header. Podemos escrever em _itálico_ e ter divisões coloridas',
    divider='green'
)

# --- Adicionar uma subheader --- #
st.subheader('Isso aqui é uma subheader. Se não informar o parâmetro _divider_ a divisão não aparece')

# --- Adicionar um texto normal --- #
st.write('''Isso é um texto normal.

Podemos colocar palavras em **negrito**

Podemos colocar palavras em *itálico*

Podemos adicionar :blue[cor]

E podemos colocar emojis :santa:!''')
