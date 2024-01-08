# --- Importar as bibliotecas --- #
import pandas as pd
import streamlit as st


def gerar_graficos(tabela: object, coluna: str):
    """
    Função responsável por criar o gráfico da coluna selecionada.
    :param tabela: DataFrame com os dados.
    :param coluna: Coluna selecionada.
    """
    # --- Realizar a contagem dos valores da coluna selecionada --- #
    df = tabela[coluna].value_counts()

    # --- Criar o gráfico e colocar no site --- #
    st.bar_chart(df)
