# --- Importar a biblioteca --- #
import streamlit as st

# --- Título à página --- #
st.title('Aula #08 - Menu lateral')

# --- Adicionar escrita na barra lateral --- #
st.sidebar.title('Menu')

# --- Adicionar uma entrada de texto --- #
texto = st.sidebar.text_input(
    label='Entrada',
    placeholder='Escreva algo'
)

# --- Lista com valores para a caixa de seleção --- #
lista_linguagens = [
    'C',
    'C#',
    'Python',
    'Java'
]

# --- Caixa de seleção --- #
linguagens = st.sidebar.selectbox(
    label='Linguagens de programação',
    options=lista_linguagens,
    placeholder='Selecione uma opção',
    index=None
)

# --- Botão de seleção múltipla --- #
st.sidebar.write('Escolha quais frutas você gosta:')
fruta_1 = st.sidebar.checkbox('Maçã')
fruta_2 = st.sidebar.checkbox('Pêra')
fruta_3 = st.sidebar.checkbox('Uva')

# --- Lista com os valores para o botão de seleção única --- #
lista_opcoes = [
    'Barra lateral',
    'Página do site'
]

# --- Botão de seleção única --- #
opcoes = st.sidebar.radio(
    label='Escolha uma opção:',
    options=lista_opcoes,
    horizontal=True
)

# --- Botão de enviar --- #
enviar = st.sidebar.button('Enviar')
if enviar:
    # Escrever na barra lateral
    if opcoes == 'Barra lateral':
        st.sidebar.subheader('Escrever na barra lateral:')
        st.sidebar.write(texto)
        st.sidebar.write(linguagens)
        if fruta_1:
            st.sidebar.write('Maçã')
        if fruta_2:
            st.sidebar.write('Pêra')
        if fruta_3:
            st.sidebar.write('Uva')

    # Escrever na página do site
    if opcoes == 'Página do site':
        st.subheader('Escrever na barra lateral:')
        st.write(texto)
        st.write(linguagens)
        if fruta_1:
            st.write('Maçã')
        if fruta_2:
            st.write('Pêra')
        if fruta_3:
            st.write('Uva')
