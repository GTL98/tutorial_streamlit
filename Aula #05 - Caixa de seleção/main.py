# --- Importar a biblioteca --- #
import streamlit as st

# --- Criar uma lista com os dados para a caixa de seleção --- #
dados = [
    'Maçã',
    'Banana',
    'Pêra',
    'Uva',
    'Melancia'
]

# --- Título na página --- #
st.title('Aula #05 - Caixa de seleção')

# --- Criar a caixa de seleção --- #
selecionar_frutas = st.selectbox(
    label='Frutas',  # informação acima da caixa de seleção
    options=dados,  # lista com os dados
    placeholder='Escolha uma opção',  # texto base informativo na caixa de seleção
    index=None  # impede que o primeiro item da lista seja o item padrão da caixa, com isso o texto em "placeholder" aparece
)

# --- Escrever a informação selecionada --- #
st.subheader(f'A fruta que você selecionou foi: {selecionar_frutas}')
