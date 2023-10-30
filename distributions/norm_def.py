import math
import plotly.express as px
import numpy

def norm_pad(n, mean, devPad):
# n = 50
# media = 25
# devpad = 7
    lista = []
    for i in range(1, n):
        try:
            z = (i - mean) / (devPad)
            valor = (1 / ((2 * math.pi) ** 1/2)) * (math.e ** (-1/2 * (z ** 2)))
            lista.append(valor)
        except:
            z = 0
            valor = 0 
            lista.append(valor)
    fig = px.line(lista, width=800, height=500, title = 'Função de Probabilidade Normal Padrão', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable': 'Probabilidade'}, line_shape='spline')
    fig.update_traces(marker={'color': 'green'})
    return fig 

def norm_pad_accum(n, mean, devPad):
    lista = []
    valor = 0
    for i in range(1, n):
        try:
            z = (i - mean) / (devPad)
            valor = valor + (1 / ((2 * math.pi) ** 1/2)) * (math.e ** (-1/2 * (z ** 2)))
            lista.append(valor)
        except:
            z = 0
            valor = 0 
            lista.append(valor)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição Normal Padrão', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(line_color='green')
    return fig
