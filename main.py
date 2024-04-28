import streamlit as st
import pandas as pd
import plotly_express as px

st.set_page_config(layout="wide")
st.title("Centro de Suprimentos do Abastecimento")
st.subheader("Gerência de Suprimentos - VIATURAS")

# Carregando o DataFrame a partir do arquivo Excel
df = pd.read_excel("VTR.xlsx")

# Gráfico com filtro
st.sidebar.title("Filtro")
ano_selecionado = st.sidebar.selectbox("Ano", df["Ano"].unique())
modelos_selecionados = st.sidebar.multiselect("Modelo Viatura", df["Modelo Viatura"].unique(), default=[df["Modelo Viatura"].unique()[0]])

df_filtrado = df[(df["Ano"] == ano_selecionado) & (df["Modelo Viatura"].isin(modelos_selecionados))]

fig1 = px.bar(df_filtrado, x="Modelo Viatura", y=["PO", "EO"], barmode="group", title=f"Comparação entre PO e EO para o ano - [UTILIZE A BARRA LATERAL] {ano_selecionado}")

# Gráfico sem filtro
fig2 = px.bar(df, x="Ano", y=["PO", "EO"], color_discrete_map={'PO':'blue', 'EO':'red'},
              title="Comparação entre PO e EO por Ano",
              labels={"value": "Valor", "variable": "Tipo", "Ano": "Ano"},
              barmode="group")

# Exibindo os gráficos
col1, col2 = st.columns(2)
col1.plotly_chart(fig1, use_container_width=True)
col2.plotly_chart(fig2, use_container_width=True)

st.write("Conforme os dados analisados no gráfico, a Estima de Obtenção para o TIPO 03 é x.")
st.write("Cabe ressaltar, que foram adicionados, os valores das viaturas com vida útil vencidas")
