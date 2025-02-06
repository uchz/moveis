import streamlit as st
import pandas as pd

# Carregar os dados do Excel
@st.cache_data
def carregar_dados():
    df = pd.read_excel("moveis2.xlsx")
    df.columns = df.columns.str.strip()
    
    # Formatando os preços
    df["Preço final"] = df["Preço final"].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    
    return df[["Nome", "Preço final", "Descrição"]]

df = carregar_dados()

# Estilo personalizado
st.markdown("""
    <style>
        .card {
            background-color: #f8f9fa;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
        }
        .card h3 {
            color: #2c3e50;
        }
        .card p {
            margin: 5px 0;
        }
    </style>
""", unsafe_allow_html=True)

# Título do aplicativo
st.title("🔎 Pesquisa de Produtos")

# Campo de busca
pesquisa = st.text_input("Digite o nome do produto:")

# Filtrar os resultados
if pesquisa:
    resultados = df[df["Nome"].str.contains(pesquisa, case=False, na=False)]
    if not resultados.empty:
        st.write("### Resultados encontrados:")

        # Exibir os produtos como cartões
        for index, row in resultados.iterrows():
            st.markdown(f"""
                <div class="card">
                    <h3>{row['Nome']}</h3>
                    <p><b>Preço:</b> {row['Preço final']}</p>
                    <p><b>Descrição:</b> {row['Descrição']}</p>
                </div>
            """, unsafe_allow_html=True)
    else:
        st.warning("Nenhum produto encontrado.")
