# --- Importar as bibliotecas --- #
import streamlit as st
import matplotlib.pyplot as plt


def graficos(tabela: object, coluna: str, tipo: str):
    """
    Função responsável por criar os gráficos dos dados.
    :param tabela: Objeto DataFrame.
    :param coluna: Coluna a ser analisada
    :param tipo: Tipo do gráfico (pizza ou barras).
    """
    if tipo == 'pizza':
        # --- Salvar em uma variável a contagem de todos os itens da coluna --- #
        df = tabela[coluna].value_counts()

        # --- Criar o gráfico de pizza --- #
        pizza, ax = plt.subplots()
        ax.pie(
            x=df,  # variável com os valores
            labels=df.index,  # quais são os rótulos dos valores
            autopct='%1.0f%%'  # mostrar em porcentagem
        )

        # --- Colocar o título no gráfico --- #
        plt.title(coluna)

        # --- Plotar o gráfico no site --- #
        st.pyplot(pizza)

    if tipo == 'barra':
        # --- Salvar em uma variável a contagem de todos os itens da coluna --- #
        df = tabela[coluna].value_counts()

        # --- Criar o gráfico e colocar no site --- #
        st.bar_chart(df)
