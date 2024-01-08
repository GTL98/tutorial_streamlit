# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st
from gerar_grafico import gerar_graficos

# --- Adicionar título à página --- #
st.title('Projeto #02 - Dados de diabetes')
st.write('---')

# --- Ver a disposição dos dados --- #
st.header('1. Importar o banco de dados')
arquivo = 'dados_diabetes.csv'
dados = pd.read_csv(arquivo, sep=';')  # a separção é por ponto e vírgula (;)
st.write(dados.head())
st.write('---')

# --- Renomear as colunas --- #
st.header('2. Renomear as colunas')
nome_colunas = {  # dicionário com o nome antigo e nome novo
    'age': 'Idade',
    'gender': 'Sexo',
    'polyuria': 'Poliúria',
    'polydipsia': 'Sede excessiva',
    'sudden_weight_loss': 'Perda de peso',
    'weakness': 'Fraqueza',
    'polyphagia': 'Fome excessiva',
    'genital_thrush': 'Infecção por fungos',
    'visual_blurring': 'Visão borrada',
    'itching': 'Coceira',
    'irritability': 'Irritabilidade',
    'delayed_healing': 'Cura tardia',
    'partial_paresis': 'Enfraquecimento muscular',
    'muscle_stiffness': 'Rigidez muscular',
    'alopecia': 'Alopecia',
    'obesity': 'Obesidade',
    'class': 'Diabético'
}

# --- Editar o conjunto de dados --- #
dados.rename(columns=nome_colunas, inplace=True)

# --- Mostrar a tabela com os nomes das colunas trocados --- #
st.write(dados.head())
st.write('---')

# --- Criar a caixa de seleção para gerar o gráfico da coluna desejada --- #
st.header('3. Gráficos')
colunas = list(dados.columns)
coluna = st.selectbox(
    label='Colunas:',
    options=colunas,
    placeholder='Selecione uma opção',
    index=None
)

# --- Criar o botão para gerar os gráficos --- #
gerar = st.button('Gerar')
if gerar:
    # Gerar os gráficos
    gerar_graficos(dados, coluna)
