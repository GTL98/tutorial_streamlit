# --- Importar as bibliotecas --- #
import pandas as pd
import altair as alt
import streamlit as st
from PIL import Image
from gerador_dna import gerardor_dna
from contador_dna import contador_dna

# --- Abrir a imagem de capa do site --- #
capa = Image.open('./imagem/capa.png')

# --- Adicionar o título ao site --- #
st.title('Projeto #01 - Contagem de nucleotídeos')

# --- Colocar a capa no site --- #
st.image(
    capa,  # imagem
    use_column_width=True  # preencher toda a largura da tela
)
st.write('---')

# --- Obter a sequência de entrada --- #
sequencia_entrada_temp = gerardor_dna(500)
sequencia_entrada = f'>DNA aleatório \n{sequencia_entrada_temp}'  # entrada no formato FASTA

# --- Criar a área de texto para mostrar o DNA gerado --- #
area_texto = st.text_area(
    label='Sequência de entrada:',  # informação acima da caixa
    value=sequencia_entrada,  # valor incial presente na caixa
    height=250  # altura da caixa na página
)

# --- Obter somente a sequência de DNA --- #
sequencia = area_texto.splitlines()[1]
st.write('---')

# --- Mostrar qual a sequência de DNA --- #
st.header('Sequência de entrada:')
st.write(sequencia)
st.write('---')

# --- Mostrar a quantidade de cada nucleotídeo no DNA em formato de texto --- #
dic_dna = contador_dna(sequencia)
st.header('1. Quantidade de cada nucleotídeo (texto):')
st.write(f'Nessa sequência há **:red[{dic_dna["A"]}]** adeinas (A).')
st.write(f'Nessa sequência há **:red[{dic_dna["C"]}]** citosinas (C).')
st.write(f'Nessa sequência há **:red[{dic_dna["G"]}]** guaninas (G).')
st.write(f'Nessa sequência há **:red[{dic_dna["T"]}]** timinas (T).')
st.write('---')

# --- Mostrar a quantidade de cada nucleotídeo no DNA em um DataFrame (tabela) --- #
st.header('2. Quantidade de cada nucleotídeo (tabela):')
tabela = pd.DataFrame.from_dict(  # criar a tabela
    dic_dna,
    orient='index'
)
tabela = tabela.rename(  # renomear a coluna das quantidades
    mapper={0: 'Quantidade'},
    axis='columns',
)
tabela.reset_index(inplace=True)  # o índice deixa de ser os nucleotídeos
tabela = tabela.rename(  # renomear as colunas dos nicleotídeos
    columns={'index': 'Nucleotídeos'}
)
st.write(tabela)
st.write('---')

# --- Mostrar a quantidade de cada nucleotídeo no DNA em um gráfico --- #
st.header('3. Quantidade de cada nucleotídeo (gráfico):')
grafico = alt.Chart(tabela).mark_bar().encode(  # criar o gráfico
    x='Nucleotídeos',
    y='Quantidade'
)
grafico = grafico.properties(
    width=alt.Step(100)  # controla a largura do gráfico
)
st.write(grafico)
