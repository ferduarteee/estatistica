import streamlit as st 
import plotly.express as px
import pandas as pd 
import math
import plotly.express as px
import numpy as np
import plotly.graph_objects as go
import scipy.stats as stats
from distributions.uniform_discrete import udisc, adisc
from streamlit_option_menu import option_menu
from hipothesis_test.statistical_significance import stats_sig
from hipothesis_test.z_table import z_table_f
from distributions.hipergeometrical import hdist, accum_hdist
from css_format import css
from distributions.bernoulli import bern_dist
from distributions.binomial import binom, binom_deg
from distributions.poisson import dpoisson
from distributions.bin_neg import bndist, ac_bndist

def main():
    with st.sidebar:
        page = option_menu("Menu Principal", ['Página Inicial', 'Distribuições'],#,'Significância Estatística', 'Tabela Z'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=0)
    if page == "Página Inicial":
        initial()
    elif page == "Significância Estatística":
        significance_page()
    elif page == "Tabela Z":
        z_table_page()
    elif page == "Distribuições":
        distributions_page()

def initial():
    css()
    st.write("Programa desenvolvido por Fernando Duarte no projeto Edital nº 69/2022")
    col1, col2= st.columns([40, 1])
    with col1:
        st.header("Departamento Acadêmico de Estatística")
    with col2:
        st.image("https://www.utfpr.edu.br/icones/cabecalho/logo-utfpr/@@images/efcf9caf-6d29-4c24-8266-0b7366ea3a40.png", width = 200)
    st.write('\n')
    st.subheader("Essa página se dedica à demonstração de Data Apps didáticos orientados aos discentes de disciplinas do Departamento Acadêmico de Estatística da UTFPR")
    st.header('\n')
    st.header('\n')
    st.header('\n')
    col1, col2 = st.columns([3,1])
    with col1:
        st.image("https://www.mathwarehouse.com/animated-gifs/images/calculus/reinmann-sum-animation.gif", width = 400)
    with col2: 
        st.image("https://www.mathwarehouse.com/animated-gifs/images/pythagorean-theorem-sum-of-squares-demonstration-gif-2.gif", width = 300)

        
def significance_page():
    st.write("Programa desenvolvido por Fernando Duarte no projeto Edital nº 69/2022")
    st.title("Nível de Significância Estatística")
    st.subheader("Selecione o valor de significância abaixo")
    nivel_de_significancia = st.slider("", 0.0, 1.0)
    fig = stats_sig(nivel_de_significancia)                                   
    st.plotly_chart(fig, use_container_width=True)


def z_table_page():
    st.write("Programa desenvolvido por Fernando Duarte no projeto Edital nº 69/2022")
    st.title("Tabela Z")
    table_z = z_table_f()
    st.dataframe(table_z, use_container_width=True, height=1125)


def distributions_page():
    st.write("Programa desenvolvido por Fernando Duarte no projeto Edital nº 69/2022")
    page = option_menu("Distribuições", ["Uniforme Discreta", "Bernoulli", "Binomial", "Hipergeométrica", "Poisson", "Binomial Negativa"], menu_icon="cast", default_index=0, orientation="horizontal")
    if page == "Uniforme Discreta":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        n = st.number_input("Insira a quantidade N (máx 100):",min_value=1, max_value=100, key = 2)
        fig = udisc(n)
        st.plotly_chart(fig, use_container_width=True)
        accumulation = st.button("Função Acumulada de Probabilidade")
        if accumulation:
           fig = adisc(n)
           st.plotly_chart(fig, use_container_width=True)
    if page == "Bernoulli":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        teta = st.slider("Insira a probabilidade:", 0.0, 1.0)
        fig = bern_dist(teta)
        st.plotly_chart(fig, use_container_width=True)
    if page == "Binomial":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        n = st.slider("Insira a quantidade N (máx 100):",min_value=1, max_value=100, key = 3)
        teta = st.slider("Insira a probabilidade:", 0.0, 1.0)
        fig = binom(teta, n)
        st.plotly_chart(fig, use_container_width=True)
        accumulation = st.button("Função Acumulada de Probabilidade")
        if accumulation:
           fig = binom_deg(teta, n)
           st.plotly_chart(fig, use_container_width=True)
    if page == "Hipergeométrica":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        N = st.number_input("Insira a quantidade N (máx 100):",min_value=1, max_value=100, key = 3)
        n = st.number_input("Insira a quantidade amostral n (máx 10):",min_value=1, max_value=10, key = 4)
        k = st.number_input("Insira a quantidade do subgrupo k (máx 25):",min_value=1, max_value=25, key = 5)
        #i = st.number_input("Insira um número de i entre 0 e 25:",min_value=1, max_value=25, key = 6)
        x = st.slider("Insira um número de eventos entre 0 e 100:", 0, 100)
        fig = hdist(N, n, k, x)
        st.plotly_chart(fig, use_container_width=True)
        accumulation = st.button("Função Acumulada de Probabilidade")
        if accumulation:
           fig = accum_hdist(N, n, k, i, x)
           st.plotly_chart(fig, use_container_width=True)
    if page =="Poisson":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        N = st.number_input("Insira a quantidade N (máx 100):",min_value=1, max_value=100, key = 5)
        p = st.slider("Insira a probabilidade", 0.0, 1.0)
        fig = dpoisson(N, p)
        st.plotly_chart(fig, use_container_width=True)
    if page =="Binomial Negativa":
        st.title("Distribuições")
        st.write("\n")
        st.write("\n")
        r = st.number_input("Insira um r (máx 20):", 0, 20, key = 101)
        x = st.slider("Insira a quantidade N (máx 100):", 0, 100, key = 100)
        teta = st.slider("Insira a probabilidade", 0.0, 1.0, key = 102)
        fig = bndist(r, x, teta)
        st.plotly_chart(fig, use_container_width=True)
        accumulation = st.button("Função Acumulada de Probabilidade")
        if accumulation:
           fig = ac_bndist(r, x, teta)
           st.plotly_chart(fig, use_container_width=True)
if __name__ == "__main__":
    main()





















