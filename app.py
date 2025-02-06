import streamlit as st
import pandas as pd

# Carregar os dados do Excel
@st.cache_data
def carregar_dados():
    df = pd.read_excel("moveis2.xlsx")  # Substitua pelo nome correto do arquivo
    
    # Removendo espaços em branco nos nomes das colunas (caso existam)
    df.columns = df.columns.str.strip()

    # Formatando os preços para exibir corretamente o "R$"
    df["Preço final"] = df["Preço final"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    return df[["Nome", "Preço final", "Descrição"]]  # Mantém apenas as colunas desejadas

df = carregar_dados()

# Título do aplicativo
st.title("🔎 Pesquisa de Produtos")

# Campo de busca
pesquisa = st.text_input("Digite o nome do produto:")

# Filtrar os resultados
if pesquisa:
    resultados = df[df["Nome"].str.contains(pesquisa, case=False, na=False)]
    if not resultados.empty:
        st.write("### Resultados encontrados:")
        st.dataframe(resultados, hide_index=True, use_container_width=True)  # Esconde o índice da tabela
    else:
        st.warning("Nenhum produto encontrado.")
    