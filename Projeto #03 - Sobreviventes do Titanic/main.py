# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st
from graficos import graficos

# --- Título no site --- #
st.title('Projeto #03 - Sobreviventes do Titanic')
st.write('---')

# --- Importar o arquivo --- #
st.header('1. Importar os dados')
arquivo = './titanic_dados.csv'

# --- Ler o arquivo --- #
dados = pd.read_csv(arquivo)

# --- Mostrar os dados no site --- #
st.write(dados.head())
st.write('---')

# --- Analisar as colunas --- #
st.header('2. Analisar as colunas')
dados.info()

# --- Criar colunas para as tabelas --- #
col_1, col_2 = st.columns(2)

# --- Colunas antes da limpeza --- #
with col_1:
    st.subheader('Antes')
    st.write(dados.columns)

# --- Retirar as colunas que não fazem sentido para a análise --- #
dados.drop(
    [
        'PassengerId',
        'Name',
        'Ticket',
        'Cabin'
    ],
    axis=1,  # retirar as colunas com os nomes da lista
    inplace=True  # mexe diretamente na tabela
)

# --- Colunas depois da limpeza --- #
with col_2:
    st.subheader('Depois')
    st.write(dados.columns)
st.write('---')

# --- Remover os valores nulos das linhas --- #
st.header('3. Remover os valores nulos')

# --- Retirar as linhas que possuem ao menos 1 valor nulo --- #
dados.dropna(
    axis=0,  # retirar os valores nulos nas linhas
    how='any',  # ao menos 1 valor nulo na linha
    inplace=True  # mexe diretamente na tabela
)
st.write(dados.head())
st.write('---')

# --- Obter a estatística dos dados --- #
st.header('4. Estatística dos dados')

# --- Escrever no formato de tabela a estatística dos dados --- #
st.write(dados.describe().T)

# --- Verificar se há somente "male" e "female" na coluna "Sex" --- #
st.write(dados['Sex'].unique())
st.write('---')

# --- Renomear as colunas --- #
st.header('5. Renomear as colunas')
# --- Criar as colunas para dispor as informações --- #
col_1, col_2 = st.columns(2)

# --- Colunas antes da renomeação --- #
with col_1:
    st.subheader('Antes')
    st.write(dados.columns)

# --- Mudar o nome das colunas para português --- #
nome_colunas = {
    'Survived': 'Sobreviveu',
    'Pclass': 'Classe',
    'Sex': 'Gênero',
    'Age': 'Idade',
    'SibSp': 'Irmãos/Casal',
    'Parch': 'Pais/Filhos',
    'Fare': 'Tarifa',
    'Embarked': 'Embarque'
}
dados.rename(
    columns=nome_colunas,  # dicionário com a mudança dos nomes
    inplace=True  # mudar diretamente na tabela
)

# --- Colunas depois da renomeação --- #
with col_2:
    st.subheader('Depois')
    st.write(dados.columns)
st.write('---')

# --- Criar os gráficos --- #
st.header('6. Mostrar em forma de gráfico os dados')

# --- Criar uma lista com todas as colunas --- #
colunas = list(dados.columns)

# --- Criar uma caixa de seleção para escolher a coluna --- #
coluna = st.selectbox(
    label='Escolha uma opção:',
    options=colunas,
    placeholder='Selecione uma coluna',
    index=None
)
# --- Criar listas para separar o tipo de gráfico --- #
lista_pizza = ['Sobreviveu', 'Classe', 'Gênero', 'Embarque']
lista_barra = ['Idade', 'Tarifa', 'Irmãos/Casal', 'Pais/Filhos']

# --- Plotar os gráficos --- #
if coluna in lista_pizza:
    graficos(dados, coluna, 'pizza')
if coluna in lista_barra:
    graficos(dados, coluna, 'barra')
