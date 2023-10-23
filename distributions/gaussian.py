import math
import plotly.express as px
 

def gaussian(x, mi, var):
    lista = list()
    for i in range(x):
        fx = ((math.e ** (-0.5 * (((i - mi) / var) ** 2))) / ((2 * math.pi * (var ** 2)) ** 0.5))
        lista.append(fx)
    fig = px.scatter(lista, width=900, height=500, title = 'Função de Densidade Normal', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'})
    fig.update_traces(marker={'color': 'green'})
    return fig 

def ac_gaussian(x, mi, var):
    lista = list()
    fx = 0
    for i in range(x):
        fx = fx + ((math.e ** (-0.5 * (((i - mi) / var) ** 2))) / ((2 * math.pi * (var ** 2)) ** 0.5))
        lista.append(fx)
    fig = px.line(lista, width=900, height=500, title = 'Função de Distribuição Normal', labels={'value': 'Probabilidade', 'index':'Eventos', 'variable':'Probabilidade'}, line_shape='hv')
    fig.update_traces(marker={'color': 'green'})
    return fig