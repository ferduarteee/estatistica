import streamlit as st 
import plotly.express as px
import pandas as pd 
import math
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
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

def main():
    with st.sidebar:
        page = st.radio("Navegar", ("Página Inicial","Distribuições", "Significância Estatística", "Tabela Z"))
    if page== "Página Inicial":
        initial()
    elif page == "Significância Estatística":
        show_page_1()
    elif page == "Tabela Z":
        show_page_2()
    elif page == "Distribuições":
        show_page_3()

def initial():
    col1, col2= st.columns([5, 1])
    with col1:
        st.header("Departamento Acadêmico de Estatística")
    with col2:
        st.image("https://www.utfpr.edu.br/icones/cabecalho/logo-utfpr/@@images/efcf9caf-6d29-4c24-8266-0b7366ea3a40.png", width = 200)
    st.subheader('\n')
    st.subheader('\n')
    st.subheader('\n')
    st.subheader("Essa página se dedica à demonstração de Data Apps didáticos orientados aos discentes de disciplinas do Departamento Acadêmico de Estatística da UTFPR")
        
def show_page_1():
    st.title("Nível de Significância Estatística")
    graus_de_liberdade = 10
    x = np.linspace(-4, 4, 100)
    pdf = stats.t.pdf(x, graus_de_liberdade)
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=pdf, mode='lines', name='Distribuição t de Student'))
    st.subheader("Selecione o valor de significância abaixo")
    nivel_de_significancia = st.slider("", 0.0, 1.0)
    valor_critico = stats.t.ppf(1 - (nivel_de_significancia / 2), graus_de_liberdade)
    x_fill = np.linspace(min(x), -valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))
    x_fill = np.linspace(max(x), valor_critico, 100)
    y_fill = stats.t.pdf(x_fill, graus_de_liberdade)
    fig.add_trace(go.Scatter(x=np.concatenate([x_fill, x_fill[::-1]]),
                            y=np.concatenate([y_fill, np.zeros_like(y_fill)]),
                            fill='toself', fillcolor='red', line=dict(color='red', width=0),
                            name='Zona de Rejeição'))
    fig.update_layout(
        title='Distribuição t de Student com Zona de Rejeição',
        xaxis_title='Valores',
        yaxis_title='Probabilidade',
        showlegend=True
    )
    st.plotly_chart(fig, use_container_width=True)


def show_page_2():
    st.title("Tabela Z")
    table_z = create_z_table()
    st.table(table_z)

def show_page_3():
    st.title("Distribuições")
    h = True
    if h:
        def binomial(N, n):
            try:
                return ((math.factorial(N))/(math.factorial(n)*math.factorial(N - n)))
            except:
                return 0
        k = 25
        N = st.slider("", 20, 100)
        n = 10
        x = 25
        lista = list()
        for i in range(x):
            try:
                fx = (binomial(k, i) * binomial(N-k, n-i)) / binomial(N, n)
            except:
                fx = 0
            lista.append(fx)
        fig = px.scatter(lista, width=900, height=500, title = 'Função de Densidade Hipergeométrica', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
        fig.update_traces(marker={'color': 'green'})
        st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()





















