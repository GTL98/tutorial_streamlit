# --- Importar a biblioteca --- #
import streamlit as st

# --- Título da página --- #
st.title('Aula #07 - Botão de seleção múltipla')

# --- Criar a escolha do sabor da pizza --- #
st.subheader('Selecione os recheios da pizza:')
recheio_1 = st.checkbox(
    label='Calabresa'  # informação do botão
)
recheio_2 = st.checkbox('4 queijos')
recheio_3 = st.checkbox('Bacon')
recheio_4 = st.checkbox('Milho')

# --- Criar a escolha da borda recheada da pizza --- #
st.subheader('Selecione a borda recheada da pizza:')
borda_1 = st.checkbox('Catupiry')
borda_2 = st.checkbox('Cheedar')

# --- Criar um dicionário para armazenar as informações dos recheios --- #
dic_recheio = {
    'Calabresa': recheio_1,
    '4 queijos': recheio_2,
    'Bacon': recheio_3,
    'Milho': recheio_4,
}

# --- Criar um dicionário para armazenas as informações das bordas --- #
dic_borda = {
    'Catupiry': borda_1,
    'Cheedar': borda_2
}

# --- Verificar qual foram as opções selecionadas --- #
st.header('Pedido:')
st.subheader('Recheio:')
for recheio in dic_recheio.keys():
    if dic_recheio[recheio] is True:
        st.write(recheio)
st.subheader('Borda')
for borda in dic_borda.keys():
    if dic_borda[borda] is True:
        st.write(borda)
