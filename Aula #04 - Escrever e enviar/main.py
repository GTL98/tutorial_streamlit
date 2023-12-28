# --- Importar a biblioteca --- #
import streamlit as st

# --- Colocar um título --- #
st.title('Aula #04 - Escrever e enviar')

# --- Colocar o campo do texto --- #
texto = st.text_input(
    label='Campo do texto',  # título acima do campo
    placeholder='Escreva algo'  # frase que ficará como fundo do campo de texto
)

# --- Colocar a caixa de texto --- #
texto = st.text_area(
    label='Caixa de texto',  # título acima da caixa
    placeholder='Escreva algo'  # frase que ficará como fundo da caixa de texto
)

# --- Colocar o botão de enviar --- #
enviar = st.button(
    label='Enviar'  # palavra que fica no botão
)

# --- Verificar se o botão foi clicado --- #
if enviar:
    # Se clicado, mostre a frase digitada no campo
    st.write(texto)
