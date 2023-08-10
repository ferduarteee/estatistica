import streamlit as st 
import plotly.express as px
import pandas as pd 
import math
import plotly.express as px



import numpy as np
import plotly.graph_objects as go
# from scipy.stats import t
import scipy.stats as stats

def create_z_table():
    z_table = []
    for i in range(0, 31):
        z_row = []
        for j in range(0, 10):
            z_value = i / 10 + j / 100
            cumulative_prob = round(stats.norm.cdf(z_value), 4)
            z_row.append(cumulative_prob)
        z_table.append(z_row)
    return z_table


import streamlit as st
# from streamlit.pages import get_page_number

def main():
    # st.title("Aplicativo com Múltiplas Interfaces")

    # Botões para navegar entre as interfaces
    with st.sidebar:
        page = st.radio("Navegar", ("Página Inicial","Significância Estatística", "Tabela Z"))
        
    if page== "Página Inicial":
        initial()
    elif page == "Significância Estatística":
        show_page_1()
    elif page == "Tabela Z":
        show_page_2()

def initial():
    col1, col2= st.columns([5, 1])
    with col1:
        st.header("Departamento Acadêmico de Estatística")
    with col2:
        st.image("https://www.utfpr.edu.br/icones/cabecalho/logo-utfpr/@@images/efcf9caf-6d29-4c24-8266-0b7366ea3a40.png", width = 200)
        
def show_page_1():
    st.title("Nível de Significância Estatística")
    # Definindo os parâmetros da distribuição t
    graus_de_liberdade = 10

    # Gerando os valores para o eixo x
    x = np.linspace(-4, 4, 100)

    # Calculando as probabilidades correspondentes no eixo y
    pdf = stats.t.pdf(x, graus_de_liberdade)

    # Criando o gráfico
    fig = go.Figure()

    # Plotando a distribuição t de Student
    fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', name='Distribuição t de Student'))
    st.subheader("Selecione o valor de significância abaixo")
    nivel_de_significancia = st.slider("", 0.0, 1.0)

    # Calculando o valor crítico para a zona de rejeição
    valor_critico = stats.t.ppf(1 - (nivel_de_significancia / 2), graus_de_liberdade)
    
    # Criando os limites para preenchimento da área
    x_fill = np.linspace(min(x), -valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)

    # Plotando a zona de rejeição preenchida em vermelho
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))

    x_fill = np.linspace(max(x), valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)

    # Plotando a zona de rejeição preenchida em vermelho
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))

    # Configurando o layout do gráfico
    fig.update_layout(
        title='Distribuição t de Student com Zona de Rejeição',
        xaxis_title='Valores',
        yaxis_title='Probabilidade',
        showlegend=True
    )



    st.plotly_chart(fig, use_container_width=True)

    # Conteúdo da primeira página

def show_page_2():
    # Conteúdo da segunda página
    st.title("Tabela Z")

    table_z = create_z_table()

        # Criar o DataFrame a partir da tabela Z
        # df = pd.DataFrame(table_z, columns=[f"0.{j}" for j in range(10)], index=[f"{i/10:.1f}" for i in range(31)])
    st.table(table_z)



if __name__ == "__main__":
    main()





















