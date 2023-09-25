import math
import plotly.express as px
import numpy
from math import gamma, e


def qui(n, v):
    lista = []
    for i in range(1, n):
        try:
            fx = (1/(gamma(v/2) * 2 ** (v / 2))) * i ** (v/(2-1)) * e ** (- i / 2)
            lista.append(fx)
        except:
            fx = 0 
            lista.append(fx)
    fig = px.scatter(lista, width=800, height=500, title = 'Função de Probabilidade Qui-Quadrado', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable': 'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig

def qui_accum(n, v):
    fx = 0
    lista = []
    for i in range(1, n):
        try:
            fx = fx + (1/(gamma(v/2) * 2 ** (v / 2))) * i ** (v/(2-1)) * e ** (- i / 2)
            lista.append(fx)
        except:
            fx = 0 
            lista.append(fx)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição Qui-quadrada', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='green')
    return fig
