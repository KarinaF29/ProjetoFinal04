
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ip

st.set_page_config(
    page_title="Lista de Exercícios 4",
    layout="wide",
)

st.title("Projeto Final – Análise Contábil com Ajuste Econômico")
st.write("Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.")

"""1) Configure o título na barra do navegador, da página do projeto no Streamlit e descrição inicial do projeto (peso: 1,0)

- Título na barra (`page_title`): Lista de Exercícios 4
- Título da página (`header`): Projeto Final – Análise Contábil com Ajuste Econômico
- Descrição projeto (`write`): Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.
"""

st.code("""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import ipeadatapy as ip
        
st.set_page_config(
    page_title="Lista de Exercícios 4",
    layout="wide",
)

st.title("Projeto Final – Análise Contábil com Ajuste Econômico")
st.write("Este projeto tem como objetivo integrar análise de dados contábeis de empresas com indicadores econômicos, utilizando Python, Pandas, Ipeadata e Streamlit.")
""", language="python")

"""2) Importe os dados do arquivo empresas_dados.csv utilizando pandas e apresente todas as linhas da df (peso: 1,0)

Dica: Utilize `head(len(df))`
"""
st.code("""
df = pd.read_csv("empresas_dados.csv", sep=";")
# display(df.head(len(df)))
st.dataframe(df.head(len(df)))
""", language="python")

df = pd.read_csv("empresas_dados.csv", sep=";")
# display(df.head(len(df)))
st.dataframe(df.head(len(df)))

"""3) Calcule os indicadores Margem Líquida e ROA e salve como novas coluna da df. Depois apresente os dois indicadores no mesmo gráfico de linhas, agrupado por Ano  (peso: 1,0)

- Margem Líquida = Lucro Líquido / Receita Líquida * 100
- ROA = Lucro Líquido / Ativo Total *  100
"""

st.code("""
df['Margem_Liquida'] = (df['Lucro Líquido'] / df['Receita Líquida']) * 100
df['ROA'] = (df['Lucro Líquido'] / df['Ativo Total']) * 100

df_agrupado = df.groupby('Ano')[['Margem_Liquida', 'ROA']].mean().reset_index()
# display(df_agrupado)
st.dataframe(df_agrupado)

fig, ax = plt.subplots()
df_agrupado.plot(x='Ano', y='Margem_Liquida', marker="o", label='Margem Líquida', ax=ax)
df_agrupado.plot(x='Ano', y='ROA', marker="o", label='ROA', ax=ax)

ax.set_title('Margem Líquida e ROA ao Longo dos Anos')
ax.set_xlabel('Ano')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)

# plt.show()
st.pyplot(fig)     
""", language="python")

df['Margem_Liquida'] = (df['Lucro Líquido'] / df['Receita Líquida']) * 100
df['ROA'] = (df['Lucro Líquido'] / df['Ativo Total']) * 100

df_agrupado = df.groupby('Ano')[['Margem_Liquida', 'ROA']].mean().reset_index()
# display(df_agrupado)
st.dataframe(df_agrupado)

fig, ax = plt.subplots()
df_agrupado.plot(x='Ano', y='Margem_Liquida', marker="o", label='Margem Líquida', ax=ax)
df_agrupado.plot(x='Ano', y='ROA', marker="o", label='ROA', ax=ax)

ax.set_title('Margem Líquida e ROA ao Longo dos Anos')
ax.set_xlabel('Ano')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)

# plt.show()
st.pyplot(fig)

"""4) Utilize o pacote ipeadatapy e faça busca para encontrar o indicador que traga o IPCA, taxa de variação, em % e anual: (peso: 2,0)

- Baixe os dados no período de 2010 a 2024
- Altere o nome da coluna "YEAR" para "Ano"
- Altere o nome da coluna "VALUE ((% a.a.))" para "IPCA"
- Apresente a df para checar se tudo deu certo
"""
st.code("""
ip.list_series('IPCA')

ip.describe('PRECOS_IPCAG')

ipca_df = ip.timeseries('PRECOS_IPCAG', yearGreaterThan=2009, yearSmallerThan=2025)
ipca_df.rename(columns={'YEAR': 'Ano', 'VALUE ((% a.a.))': 'IPCA'}, inplace = True)
# display(ipca_df)
st.dataframe(ipca_df)
""", language="python")

ip.list_series('IPCA')

ip.describe('PRECOS_IPCAG')

ipca_df = ip.timeseries('PRECOS_IPCAG', yearGreaterThan=2009, yearSmallerThan=2025)
ipca_df.rename(columns={'YEAR': 'Ano', 'VALUE ((% a.a.))': 'IPCA'}, inplace = True)
# display(ipca_df)
st.dataframe(ipca_df)

"""5) Combine as duas df (Excel e IPEA) em uma nova df e calcule nova coluna chamada Receita Real (peso: 2,0)

- Utilize a função `pd.merge()` para unificar as duas df utiilizando a coluna Ano como conexão (chave primária) entre elas
- Crie nova coluna chamada Receita Real que será o resultado da Receita Líquida de cada ano deduzido o IPCA do ano: `Receita Real = Receitta Líquida - ( Receita Líquida * (IPCA/100) )`
- Apresente a nova df combinada
"""
st.code("""
df_combinado = pd.merge(df, ipca_df, on='Ano')
df_combinado['Receita_Real'] = df_combinado['Receita Líquida'] - (df_combinado['Receita Líquida'] * (df_combinado['IPCA'] / 100))

# display(df_combinado)
st.dataframe(df_combinado)
""", language="python")

df_combinado = pd.merge(df, ipca_df, on='Ano')
df_combinado['Receita_Real'] = df_combinado['Receita Líquida'] - (df_combinado['Receita Líquida'] * (df_combinado['IPCA'] / 100))

# display(df_combinado)
st.dataframe(df_combinado)

"""6) Crie gráfico de linha que apresente as variáveis Receita Líquida e Receita Real ao longo dos anos (no mesmo gráfico) (peso: 1,0)"""

st.code("""
df_agrupado = df_combinado.groupby('Ano')[['Receita Líquida', 'Receita_Real']].sum().reset_index()
# display(df_agrupado)
st.dataframe(df_agrupado)

fig, ax = plt.subplots()
df_agrupado.plot(x='Ano', y='Receita Líquida', label='Receita Líquida', ax=ax)
df_agrupado.plot(x='Ano', y='Receita_Real', label='Receita Real', ax=ax)
ax.set_title('Receita Líquida e Receita Real ao Longo dos Anos')
ax.set_xlabel('Ano')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)
# plt.show()
st.pyplot(fig)
""", language="python")

df_agrupado = df_combinado.groupby('Ano')[['Receita Líquida', 'Receita_Real']].sum().reset_index()
# display(df_agrupado)
st.dataframe(df_agrupado)

fig, ax = plt.subplots()
df_agrupado.plot(x='Ano', y='Receita Líquida', label='Receita Líquida', ax=ax)
df_agrupado.plot(x='Ano', y='Receita_Real', label='Receita Real', ax=ax)
ax.set_title('Receita Líquida e Receita Real ao Longo dos Anos')
ax.set_xlabel('Ano')
ax.set_ylabel('Valor')
ax.legend()
ax.grid(True)
# plt.show()
st.pyplot(fig)

"""7) Faça os ajustes necessários e leve este projeto para a web usando GitHub e Streamlit (peso: 2,0)

- Caça os ajustes necessários no projeto para ser publicado no Streamlit
- Crie novo repositório público no GitHub e leve os arquivos .py e .csv pra lá. Aproveite e crie o arquivo requirements.txt com os pacotes utilizados no projeto
- Crie novo projeto no Streamlit e associe ao repositório da lista
"""
