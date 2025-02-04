import streamlit as st
import pandas as pd

# Carregar os dados do Excel
@st.cache_data
def carregar_dados():
    df = pd.read_excel("moveis.xlsx")  # Substitua pelo nome correto do arquivo
    return df[["Nome", "Preço Final",'Cor']]  # Mantém apenas as colunas desejadas

df = carregar_dados()

# Título do aplicativo
st.title("🔎 Pesquisa de Produtos")

# Campo de busca
pesquisa = st.text_input("Digite o nome do produto:")

# Filtrar os resultados
if pesquisa:
    resultados = df[df["Nome"].str.contains(pesquisa, case=False, na=False)]
    if not resultados.empty:
        st.write("Resultados encontrados:")
        st.dataframe(resultados)
    else:
        st.warning("Nenhum produto encontrado.")
