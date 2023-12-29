# --- Importar a biblioteca --- #
import streamlit as st

# --- Título da página --- #
st.title('Aula #06 - Botão de seleção única')

# --- Lista com os dados --- #
lista_carros = [
    'Fiat',
    'Mercedes',
    'Volvo',
    'Chevrolet'
]

# --- Criar o botão --- #
carros = st.radio(
    label='Escolha um carro:',  # informação que fica acima das opções
    options=lista_carros,  # lista com os dados
    horizontal=True,  # a seleção das opções fica na horizontal
    index=None  # nenhuma opção fica selecionada quando a página é carregada
)

# --- Verificar se alguma opção foi selecionada --- #
if carros is None:
    # Como nenhuma opção foi selecioanda, o texto informará isso
    st.subheader('Nenhum carro foi selecionado')
else:
    # Como uma opção foi selecioanda, logo a informação disso será mostrada
    st.subheader(f'O carro selecionado foi o: {carros}')
