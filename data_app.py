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
from css_format import css

def main():
    with st.sidebar:
        page = option_menu("Menu Principal", ["Página Inicial", 'Distribuições','Significância Estatística', 'Tabela Z'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
    if page== "Página Inicial":
        initial()
    elif page == "Significância Estatística":
        significance_page()
    elif page == "Tabela Z":
        z_table_page()
    elif page == "Distribuições":
        distributions_page()

def initial():
    css()
    st.text("Programa desenvolvido por Fernando Duarte")
    col1, col2= st.columns([40, 1])
    with col1:
        st.header("Departamento Acadêmico de Estatística")
    with col2:
        st.image("https://www.utfpr.edu.br/icones/cabecalho/logo-utfpr/@@images/efcf9caf-6d29-4c24-8266-0b7366ea3a40.png", width = 200)
    st.subheader('\n')

    st.subheader("Essa página se dedica à demonstração de Data Apps didáticos orientados aos discentes de disciplinas do Departamento Acadêmico de Estatística da UTFPR")
        
def significance_page():
    st.title("Nível de Significância Estatística")
    st.subheader("Selecione o valor de significância abaixo")
    nivel_de_significancia = st.slider("", 0.0, 1.0)
    fig = stats_sig(nivel_de_significancia)                                   
    st.plotly_chart(fig, use_container_width=True)


def z_table_page():
    st.title("Tabela Z")
    table_z = z_table_f()
    st.table(table_z)

def distributions_page():
    page = option_menu("Distribuições", ["Uniforme Discreta", "Bernoulli", "Binomial"], menu_icon="cast", default_index=2, orientation="horizontal")
    if page == "Uniforme Discreta":
        st.title("Distribuições")
        n = st.number_input("Insira um número de eventos entre 0 e 100:",min_value=1, max_value=100, key = 2)
        fig = udisc(n)
        st.plotly_chart(fig, use_container_width=True)
        accumulation = st.button("Função Acumulada de Probabilidade")
        if accumulation:
           fig = adisc(n)
           st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()





















