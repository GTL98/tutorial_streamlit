# --- Importar a biblioteca --- #
import streamlit as st

# --- Colocar um título na página --- #
st.title('Página de widgets')
st.write('---')

# --- Criar a lista com as opções para a caixa de seleção --- #
lista_frutas = [
    'Maçã',
    'Pêra',
    'Uva',
    'Melancia'
]

# --- Criar a caixa de seleção --- #
fruta = st.selectbox(
    label='Selecione:',
    options=lista_frutas,
    placeholder='Selecione uma fruta',
    index=None
)

# --- Criar os checkboxes --- #
st.write('Qual clima você gosta?')
calor = st.checkbox('Calor')
frio = st.checkbox('Frio')

# --- Criar a lista para os botões de escolha única --- #
lista_carros = [
    'Fiat',
    'Mercedes',
    'Volvo',
    'Chevrolet'
]

# --- Criar os botões de escolha única --- #
carro = st.radio(
    label='Escolha um carro:',
    options=lista_carros,
    index=None,
    horizontal=True
)

# --- Criar a caixa de texto --- #
texto = st.text_input('Digite o seu nome:')

# --- Criar o botão de envio --- #
enviar = st.button('Enviar')
if enviar:
    if calor:
        st.write(f'''Nome: {texto}
        
Carro: {carro}
    
Clima: Calor
    
Fruta: {fruta}
''')

    if frio:
        st.write(f'''Nome: {texto}

Carro: {carro}

Clima: Frio

Fruta: {fruta}
''')
